---
title: "ESP32 Weather Station – PCBs Rev0 Arrived and, Well, It's No Bueno"
date: 2025-05-30 18:00:00 +0200
categories: [projects]
tags: [esp32, pcb, jlcpcb, kicad, hardware, lessons-learned]
layout: post
---

# 📦 ESP32 Weather Station – PCBs Rev0 Arrived and, Well, It's No Bueno

Great news — the **Rev0 PCBs** for the ESP32 Weather Station project have arrived from [JLCPCB.com](https://jlcpcb.com), and the quality is absolutely stunning!

💸 **The cost?** Just **4 Euros for 5 pieces** — shipping included. Honestly, I’m still amazed by what you can get for that price.

---

![Rev0 PCB Front](/assets/img/esp32-mark0/rev0-front.jpg)

Excited by how they turned out, I immediately began soldering. The **pre-soldered pad finish** made it a joy to work with — everything flowed smoothly, and the **precision pin sockets** went in without trouble.

But then... I noticed something.

---

![Rev0 Populated](/assets/img/esp32-mark0/rev0-populated.jpg)

Yeah. That’s a bit of a **collision** between the **NodeMCU board** and the **eInk display**. They physically *don’t* fit well together on the current layout. A rookie mistake — but that’s what Rev0 is for: learning.

So, I fired up **KiCAD** again, reworked the layout, and placed an order for **Rev1**. This time in **white**, still elegant — but now visually distinguishable from the black Rev0 boards.

---

## 🧠 Visual Recap from KiCAD

Here’s a look at the Rev0 board design — **top layer**, **bottom layer**, and **3D render**, all side by side:

<div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
  <img src="/assets/img/esp32-mark0/rev-1top.png" alt="Top Layer" width="32%" />
  <img src="/assets/img/esp32-mark0/rev1-bottom.png" alt="Bottom Layer" width="32%" />
  <img src="/assets/img/esp32-mark0/rev1-3d-view.png" alt="3D View" width="32%" />
</div>

---

## 🚀 Next Steps

Mistakes were made. **Lessons were learned**.  
Now I’m waiting on Rev1 — and I can’t wait to share how that one turns out.

Stay tuned!
