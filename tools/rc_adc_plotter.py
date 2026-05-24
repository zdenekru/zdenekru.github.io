#!/usr/bin/env python3
"""Tiny Tkinter viewer for Zdenduino RC discharge CSV serial output."""

from __future__ import annotations

import queue
import re
import threading
import time
import tkinter as tk
from tkinter import ttk

try:
    import serial
    from serial.tools import list_ports
except ImportError:  # pragma: no cover - depends on local machine packages
    serial = None
    list_ports = None


CSV_RE = re.compile(r"^\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9.]+)\s*$")


class RcAdcPlotter(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Zdenduino RC ADC Plotter")
        self.geometry("920x560")
        self.minsize(760, 440)

        self.samples: list[tuple[int, int, float]] = []
        self.messages: "queue.Queue[tuple[str, object]]" = queue.Queue()
        self.stop_event = threading.Event()
        self.reader_thread: threading.Thread | None = None
        self.serial_handle = None

        self.port_var = tk.StringVar()
        self.baud_var = tk.StringVar(value="115200")
        self.status_var = tk.StringVar(value="Disconnected")
        self.latest_var = tk.StringVar(value="No samples yet")

        self._build_ui()
        self._refresh_ports()
        self.after(50, self._process_messages)

    def _build_ui(self) -> None:
        controls = ttk.Frame(self, padding=10)
        controls.pack(fill=tk.X)

        ttk.Label(controls, text="Port").pack(side=tk.LEFT)
        self.port_combo = ttk.Combobox(controls, textvariable=self.port_var, width=24)
        self.port_combo.pack(side=tk.LEFT, padx=(6, 12))

        ttk.Button(controls, text="Refresh", command=self._refresh_ports).pack(side=tk.LEFT)

        ttk.Label(controls, text="Baud").pack(side=tk.LEFT, padx=(18, 0))
        ttk.Entry(controls, textvariable=self.baud_var, width=8).pack(side=tk.LEFT, padx=(6, 12))

        self.connect_button = ttk.Button(controls, text="Connect", command=self._connect)
        self.connect_button.pack(side=tk.LEFT)

        ttk.Button(controls, text="Clear", command=self._clear).pack(side=tk.LEFT, padx=(8, 0))

        ttk.Label(controls, textvariable=self.status_var).pack(side=tk.RIGHT)

        self.canvas = tk.Canvas(self, bg="#111318", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 8))
        self.canvas.bind("<Configure>", lambda _event: self._draw())

        footer = ttk.Frame(self, padding=(10, 0, 10, 10))
        footer.pack(fill=tk.X)
        ttk.Label(footer, textvariable=self.latest_var).pack(side=tk.LEFT)

    def _refresh_ports(self) -> None:
        if list_ports is None:
            self.port_combo["values"] = []
            self.status_var.set("pyserial is missing: pip install pyserial")
            return

        ports = [port.device for port in list_ports.comports()]
        self.port_combo["values"] = ports
        if ports and not self.port_var.get():
            self.port_var.set(ports[0])

    def _connect(self) -> None:
        if self.reader_thread and self.reader_thread.is_alive():
            self._disconnect()
            return

        if serial is None:
            self.status_var.set("Install pyserial first: pip install pyserial")
            return

        port = self.port_var.get().strip()
        if not port:
            self.status_var.set("Select a serial port")
            return

        try:
            baud = int(self.baud_var.get())
        except ValueError:
            self.status_var.set("Invalid baud rate")
            return

        self.stop_event.clear()
        self.reader_thread = threading.Thread(
            target=self._read_serial,
            args=(port, baud),
            daemon=True,
        )
        self.reader_thread.start()
        self.connect_button.configure(text="Disconnect")

    def _disconnect(self) -> None:
        self.stop_event.set()
        if self.serial_handle is not None:
            try:
                self.serial_handle.close()
            except Exception:
                pass
        self.serial_handle = None
        self.connect_button.configure(text="Connect")
        self.status_var.set("Disconnected")

    def _read_serial(self, port: str, baud: int) -> None:
        try:
            with serial.Serial(port, baud, timeout=0.2) as ser:
                self.serial_handle = ser
                self.messages.put(("status", f"Connected to {port}"))
                time.sleep(1.5)
                ser.reset_input_buffer()

                while not self.stop_event.is_set():
                    line = ser.readline().decode("utf-8", errors="replace").strip()
                    match = CSV_RE.match(line)
                    if match:
                        self.messages.put(
                            (
                                "sample",
                                (
                                    int(match.group(1)),
                                    int(match.group(2)),
                                    float(match.group(3)),
                                ),
                            )
                        )
                    elif line:
                        self.messages.put(("status", line))
        except Exception as exc:
            self.messages.put(("status", f"Serial error: {exc}"))
        finally:
            self.serial_handle = None
            self.messages.put(("disconnected", None))

    def _process_messages(self) -> None:
        changed = False

        while True:
            try:
                kind, payload = self.messages.get_nowait()
            except queue.Empty:
                break

            if kind == "sample":
                sample = payload
                self.samples.append(sample)
                self.samples = self.samples[-240:]
                self.latest_var.set(
                    f"time={sample[0]} ms   raw={sample[1]}   voltage={sample[2]:.3f} V"
                )
                changed = True
            elif kind == "status":
                self.status_var.set(str(payload))
            elif kind == "disconnected":
                self.connect_button.configure(text="Connect")

        if changed:
            self._draw()

        self.after(50, self._process_messages)

    def _clear(self) -> None:
        self.samples.clear()
        self.latest_var.set("No samples yet")
        self._draw()

    def _draw(self) -> None:
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        if width < 20 or height < 20:
            return

        pad_left = 58
        pad_right = 18
        pad_top = 22
        pad_bottom = 42
        plot_w = width - pad_left - pad_right
        plot_h = height - pad_top - pad_bottom

        self.canvas.create_rectangle(
            pad_left,
            pad_top,
            pad_left + plot_w,
            pad_top + plot_h,
            outline="#2b303a",
        )

        for volts in (0.0, 1.1, 2.2, 3.3):
            y = pad_top + plot_h - (volts / 3.3) * plot_h
            self.canvas.create_line(pad_left, y, pad_left + plot_w, y, fill="#242a33")
            self.canvas.create_text(
                pad_left - 10,
                y,
                text=f"{volts:.1f}V",
                fill="#aeb6c2",
                anchor=tk.E,
                font=("TkDefaultFont", 9),
            )

        self.canvas.create_text(
            pad_left + plot_w / 2,
            height - 16,
            text="time in current discharge window",
            fill="#aeb6c2",
            font=("TkDefaultFont", 9),
        )

        if len(self.samples) < 2:
            self.canvas.create_text(
                width / 2,
                height / 2,
                text="Waiting for CSV lines: time_ms,raw,voltage",
                fill="#d7dde8",
                font=("TkDefaultFont", 14),
            )
            return

        start = self.samples[0][0]
        end = max(self.samples[-1][0], start + 1)
        span = end - start

        points: list[float] = []
        for elapsed, _raw, voltage in self.samples:
            x = pad_left + ((elapsed - start) / span) * plot_w
            y = pad_top + plot_h - (max(0.0, min(voltage, 3.3)) / 3.3) * plot_h
            points.extend([x, y])

        self.canvas.create_line(points, fill="#4cc9f0", width=2, smooth=True)
        self.canvas.create_oval(points[-2] - 4, points[-1] - 4, points[-2] + 4, points[-1] + 4, fill="#f9c74f", outline="")

    def destroy(self) -> None:
        self._disconnect()
        super().destroy()


if __name__ == "__main__":
    RcAdcPlotter().mainloop()
