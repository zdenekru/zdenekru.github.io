---
title: "Starting ESP32 Weather Station Project"
date: 2025-05-26 18:00:00 +0200
categories: [projects]
tags: [esp32, iot, weather, pcb]
layout: post
---

After a period of focusing on other areas, I’ve decided to kick off a new project that brings together many of the skills I’ve been wanting to sharpen again — from PCB design to working with APIs and embedded systems. The result will be a weather station powered by an **ESP32**, designed from the ground up.

This project is meant to help me:

- 🧾 Refresh and improve my **PCB design workflow**
- 📡 Deepen my **IoT and networking** understanding
- 🧠 Push further into **C++** development for embedded
- 🔌 Work with APIs like **OpenWeatherMap**
- 🌐 Integrate OTA updates and remote control
- 🧰 Reconnect all the parts of the hardware/software stack in a cohesive way

---

## 🛠️ Mark 0 – Project Goals

The **Mark 0** version of this weather station will focus on being modular, understandable, and extensible. This phase is about learning and experimenting before moving to something smaller and more polished.

### 🔧 Design and Hardware

- Built around a **NodeMCU DevKitC** (ESP32 module)
- **100mm x 100mm** PCB — largest possible for standard JLCPCB pricing
- **All unused GPIOs exposed** via pin headers for future expandability
- Dual connectivity:
  - **USB-C** for power and serial communication
  - **Wi-Fi** for wireless functionality
- Includes a **DHT11 sensor** for **indoor temperature and humidity**

> External weather conditions will be fetched online; the DHT11 is just for monitoring the local environment (for now).

### 🧠 Features and Capabilities

- Support for **firmware updates** via USB and **OTA (Over-The-Air)**
- Weather data fetched from **OpenWeatherMap.org** via an `http.GET` API call
- Real-time display of weather data on an **ePaper display**
- Remote visualization and control through the **Blynk IoT platform**

---

## 🚧 What Comes After – Mark 1

Once Mark 0 proves its concept, the goal is to take everything learned and build a more compact, efficient version — **Mark 1**. It will be more refined in form and optimized in both hardware layout and power usage. Mark 1 will be a natural evolution, informed by real hands-on experience with the first prototype.

---

📸 **That’s all for today — tomorrow’s post will dive into the initial sketches, PCB layout decisions, and maybe even some preview photos. Stay tuned!**
