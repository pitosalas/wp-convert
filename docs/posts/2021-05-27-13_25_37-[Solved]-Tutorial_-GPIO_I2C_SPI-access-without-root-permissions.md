---
title: "[Solved] Tutorial: GPIO/I2C/SPI-access without root-permissions"
author: Pito Salas
date: 2021-05-27 13:25:37
tags:
    - gpio
    - raspberry-pi
    - howto
---


(**Web site except:** A great solution to a very specific problem I have been having! --> As you may have noticed, by default you do not have access to the GPIO-pins, the SPI-bus or the I2C-bus as a normal user and you have to use 'sudo' to access them or run an application that utilizes them; it is generally a good idea to limit access to such things for security, but on a dev-board like the UP and UP^2 it may be convenient to do development and testing as a regular user.) 
