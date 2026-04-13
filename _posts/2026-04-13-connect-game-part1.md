---
title: "Connect Game - Part 1"
date: 2026-04-13 20:00:00 +0200
categories: [projects]
tags: [Arduino, Fallout, LARP, C, game]
layout: post
image:
  path: /assets/img/connect-game/connectgametitle1.png
---

I was approached by a friend of mine, who is one of the organizers of a Fallout-themed LARP event:

👉 https://fallout.overseers.cz/

He asked me if I could help with an **in-game activity**.

And well… I *do* love a new challenge.

## Project Overview

The idea is fairly simple:

An **electronic device for a logical mini-game** used during a Fallout LARP.

The device exposes **GPIO pins and power lines**, allowing for potential future extensions and modifications.

## Project Goal

The device should support **two different game modes**:

### 1) Guided Mode

- The player has a **single wire**
- An **OLED display** shows which two GPIO pins should be connected
- The player has a limited time to connect them correctly
- After success, a **new random pair** is displayed
- After a predefined number of correct connections within a time limit, the game ends
- The player is rewarded with a **“secret”** (for example, a code)

### 2) Discovery Mode

- The player has **multiple wires**
- The correct GPIO connections must be discovered through gameplay
- Once the correct combination is connected, the device reveals the **secret**

## First Prototype

So I quickly put together *something* in **KiCad** and sent it off to PCB fabrication (**JLCPCB**).

A few weeks later, the boards arrived and… well.

I messed up 😅

Specifically, I **mirrored the GPIO extender (AW9523R)**.  
Since there were no official KiCad libraries available, I created my own footprint — and got it wrong.

![Connect Game Front](/assets/img/connect-game/connectgamefront1.jpg)

Stuff like this happens.

---

On the bright side, it gave me a chance to spend some time with a **soldering iron**.

I ended up re-soldering the GPIO extender on the other side of the board, and after some fiddling with the firmware, it *kind of* worked…

…but it was far from ideal.

![Connect Game Back](/assets/img/connect-game/connectgameback1.jpg)

## The Real Problem

The biggest issue (aside from the mirrored chip -_-) turned out to be the need for **pull-up resistors**.

For the game logic to work reliably, the GPIO pins needed to be pulled to **+5V**.

After testing everything on a **breadboard**, it finally behaved as expected.

Which means only one thing:

👉 back to PCB fabrication we go 😄

![Connect Game KiCAD V1.1](/assets/img/connect-game/connectgamekicad1.png)

---

## What's Next?

The next revision should fix:

- the **GPIO extender orientation** (lesson learned)
- proper **pull-up resistor implementation**
- overall reliability of the game logic

---

Stay tuned for **Part 2**.
