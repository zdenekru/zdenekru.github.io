---
title: "ESP32 Weather Station Mark0 – My Love/Hate Relationship with Breadboards"
date: 2025-05-27 18:00:00 +0200
categories: [projects]
tags: [esp32, blynk, prototyping, arduino]
layout: post
---

Every great electronics project starts with a tangle of jumper wires, misplaced resistors, and a moment of "why doesn't this boot anymore?" — and so it was for **Mark0**.

---

## 🛒 Getting Started

I picked up a NodeMCU ESP32 clone locally from [gme.cz](https://www.gme.cz) — the exact module is available [here](https://www.neven.cz/p/esp-wroom-32-esp32-esp-32s-2-4ghz-vyvojarska-deska-s-wifi-a-bt-38pin). It's a pretty standard 38-pin dev board with Wi-Fi and Bluetooth support.

I fired up the **Arduino IDE** (which, to be honest, is surprisingly lightweight and capable for quick embedded work), connected the board, and… ran into the usual ESP32 decision chaos.

---

## 🤖 The Board That Works (Eventually)

After trial and error, I found that selecting simply **"ESP32 Dev Module"** under **Tools → Board** is the most reliable option. Nothing fancy — just the default. Most other profiles either failed to flash or threw bizarre runtime errors.

---

## ❤️ / 💢 Love-Hate: Breadboard Edition

This is where the prototyping rollercoaster kicked in:

- ❤️ **Love**: It's hard to beat the speed and ease of breadboarding. I was blinking LEDs and reading DHT11 values within minutes.
- 💢 **Hate**: Breadboards bite back. I hit problems like random boot hangs and weird crashes — most caused by poor connections or incorrect pin layouts.

Lesson (re)learned: always double-check your GNDs and jumper wires before blaming the microcontroller.

---

## 🔄 Back to Blynk

After some time away from Blynk, I had to re-activate my subscription — now under [Blynk.io](https://blynk.io). Luckily, they’ve kept things beginner-friendly.

Using their excellent example code from [examples.blynk.cc](https://examples.blynk.cc/?board=ESP32&shield=ESP32%20WiFi&example=More%2FDHT11), I was amazed to see the app working almost instantly.

---

## 🧠 Other Features I Needed to Get Working

- **OTA Updates** (so I can flash without plugging in USB every time)
- **NTP Time Sync** (to timestamp weather data)
- **ePaper Display** with **custom fonts** (because default 8-bit style text wasn’t cutting it)

After many iterations and enough restarts to toast a PSU, I finally got this beautiful output on Serial:

```
[4132] Connected to WiFi
[4132] IP: 192.168.88.239
[4133] 
    ___  __          __
   / _ )/ /_ _____  / /__
  / _  / / // / _ \/  '_/
 /____/_/\_, /_//_/_/\_\
        /___/ v1.3.2 on ESP32



 #StandWithUkraine    https://bit.ly/swua


[4143] Connecting to blynk.cloud:80
[4274] Ready (ping: 33ms).
⏳ Waiting for time...
🕒 Time synchronized
🔄 OTA Ready!
⏰ Čas: 21:36:43
⏰ Uptime: 00:03:10
✅ Uvnitř: 23.4°C, Vlhkost: 57.0%
🌡️  Venku: 14.9°C (Pocitová: 14.3°C)
🌥️  Popis: slabý déšť
🖥️  E-Ink display updated.
```
---

## ✅ Final Thoughts

It took a lot of fiddling, patching, flashing, and debugging — but it all **works**. That’s the best kind of milestone.

📦 **Next step?** Designing the PCB! Stay tuned for updates in the next post.

