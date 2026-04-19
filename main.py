import machine
import network
import ubinascii
from machine import I2C, Pin, UART, unique_id
from umqtt.simple import MQTTClient
import utime
import json

# UART for Arduino (TX = GP0, RX = GP1)
uart = UART(0, baudrate=115200)

# Wi-Fi Configuration
ssid = "YOUR_WIFI_SSID"
password = "YOUR_WIFI_PASSWORD"

# MQTT Broker Configuration
mqtt_broker = "YOUR_MQTT_BROKER_IP"
mqtt_port = 1883
mqtt_client_id = ubinascii.hexlify(unique_id()).decode()
mqtt_topic_time = "sensor/time"

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    print("Connecting to Wi-Fi...")
    utime.sleep(1)
print("Connected to Wi-Fi:", wifi.ifconfig())

# MQTT Setup
def mqtt_connect():
    client = MQTTClient(mqtt_client_id, mqtt_broker, mqtt_port)
    client.connect()
    print("Connected to MQTT Broker:", mqtt_broker)
    return client

client = mqtt_connect()

# Real-Time Clock (RTC) Setup
rtc = machine.RTC()

def get_time_string():
    t = rtc.datetime()
    time_str = "{:02}:{:02}:{:02}".format(t[4], t[5], t[6])
    return time_str

# Main Loop
while True:
    time_str = get_time_string()
    data_time = json.dumps({"time": time_str})
    client.publish(mqtt_topic_time, data_time)
    uart_data = f"T:{time_str}\n"
    uart.write(uart_data)
    print("Sent via MQTT:", data_time)
    print("Sent to Arduino:", uart_data)
    utime.sleep(1.5)