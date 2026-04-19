
## Real-Time Clock Display System

IoT project using Raspberry Pi Pico W, Arduino Uno and LCD1602 screen.

## Tech Stack
- MicroPython (Raspberry Pi Pico W)
- Arduino C++
- MQTT protocol
- Node-RED
- UART serial communication
- I2C LCD display

## How it works
The Pico W reads time from its onboard RTC, publishes it via MQTT to Node-RED, and simultaneously sends it to Arduino via UART. Arduino displays the time on an LCD1602 screen.
