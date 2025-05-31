---
title: "Starting Mark 1 ESP32 Weather Station"
date: 2025-05-31 18:00:00 +0200
categories: [projects]
tags: [esp32, weather-station, mark1, sensors, iot, hardware]
layout: post
---

While I’m still waiting for the PCB for **Mark 0 Rev1** to arrive, I figured — why not start working on **Mark 1** already?

Yes, the naming convention might start sounding confusing (Mark 0 Rev1 vs Mark 1 Rev0 coming soon?), but hey — that’s engineering!

---

## 🧠 Let’s Add More Features!

This time, I'm going full modular. I’ll be using **a lot of modules**, probably for the last time — future iterations will reduce the number of off-the-shelf boards and become more integrated.

### 🎯 Hardware Overview for Mark 1

| Component                         | Description                  |
| --------------------------------- | ---------------------------- |
| **Microcontroller**               | ESP32 DevkitC                |
| **Temperature & Humidity Sensor** | BME680                       |
| **Light Sensor**                  | BH1750                       |
| **RTC Module**                    | DS3231                       |
| **Motion Sensor (PIR)**           | HC-SR501                     |
| **Battery**                       | 18650 Li-ion                 |
| **Battery Management System**     | TP4056 (with protection)     |
| **Display**                       | ILI9488 3.5” TFT Touchscreen |
| **Enclosure**                     | 3D Printed, wall-mounted     |

---

## 📌 ESP32 DevKitC 30-Pin GPIO Pin Map

Pin budget is **tight** for this application, but according to this map, it should work out — just barely. R&D is full of surprises though, so... fingers crossed 🤞.

| Peripheral / Module            | Function            | Suggested GPIO(s)                | Notes                |
| ------------------------------ | ------------------- | -------------------------------- | -------------------- |
| **ILI9488 Display**            | SPI MOSI            | `GPIO23`                         | SPI Bus              |
|                                | SPI CLK             | `GPIO18`                         | SPI Bus              |
|                                | SPI CS (TFT)        | `GPIO15`                         | Chip Select          |
|                                | D/C                 | `GPIO2`                          | Data/Command control |
|                                | RESET (opt.)        | `GPIO4`                          | Can tie high         |
|                                | Backlight Control   | `GPIO21`                         | PWM capable          |
| **Touch Controller (XPT2046)** | SPI MISO            | `GPIO19`                         | SPI MISO shared      |
|                                | Touch CS            | `GPIO5`                          | Separate CS          |
| **BME680**                     | I2C SDA             | `GPIO22`                         | Shared I2C           |
|                                | I2C SCL             | `GPIO21`                         | Shared I2C           |
| **BH1750**                     | I2C                 | (Shared)                         | Same bus as BME680   |
| **DS3231 RTC**                 | I2C                 | (Shared)                         | Same bus as BME680   |
| **PIR Sensor (HC-SR501)**      | Digital Input       | `GPIO33`                         | Input-only pin       |
| **Button #1**                  | Digital Input       | `GPIO25`                         | With pull-up         |
| **Button #2**                  | Digital Input       | `GPIO26`                         | Optional             |
| **Status LED**                 | Digital Output      | `GPIO27`                         | Any GPIO             |
| **Battery Voltage Sense**      | Analog Input (ADC1) | `GPIO35`                         | via voltage divider  |
| **Expansion / Future Use**     | Breakout Header     | `GPIO12`, `13`, `14`, `16`, `17` | Available            |

### 🧠 Visual Map:

```
            +--------------------------+
3.3V      --|  EN             GPIO23   |-- MOSI (TFT)           
            |  VP             GPIO22   |-- I2C SDA (BME680, etc.)
5V        --|  VIN            GPIO1    |-- TX0 (USB Serial)
Free      --|  GPIO34         GPIO3    |-- RX0 (USB Serial)
ADC       --|  GPIO35         GPIO21   |-- I2C SCL / Backlight
Battery   --|  GPIO32         GPIO19   |-- MISO (Touch)
PIR       --|  GPIO33         GPIO18   |-- CLK (TFT)
Button1   --|  GPIO25         GPIO5    |-- Touch CS
Button2   --|  GPIO26         GPIO17   |-- Free / Expansion
StatusLED --|  GPIO27         GPIO16   |-- Free / Expansion
Free      --|  GPIO14         GPIO4    |-- RESET (TFT)
Free      --|  GPIO12         GPIO2    |-- D/C (TFT)
Free      --|  GPIO13         GPIO15   |-- TFT CS
GND       --|  GND            GND      |-- GND
4V        --|  VIN            3V3      |-- 3.3V        
            +--------------------------+
```

---

## 🛠️ End Goals for Mark 1

This isn’t just a prototype — I want this to start feeling **like a product**. So:

- ✅ Use **JLCPCB + PCBA** services for at least partial assembly  
  I love soldering, but I also want to learn how to **order production-ready PCBs**. This will help me scale things in the future.

- ✅ All-in-one **neat and compact package**

- ✅ Mounted in a custom **3D printed case** — *VEGA* style  
  (i.e. wall-mounted, and easy to take off for charging or updating)

- ✅ **Expandable design** — all unused GPIOs available via **pin headers**

- ✅ Possibly add an **external weather node**  
  Using another BME680 + ESP32 via **Zigbee or MQTT** to report outside data wirelessly.

---

Next step: ordering all the modules from China and preparing to test and integrate them as they arrive.

Stay tuned for unboxings, wiring, tests, and all the fun that comes with it!
