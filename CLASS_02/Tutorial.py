from time import sleep
from machine import Pin

led = Pin(2, Pin.OUT)

try:
    while True:
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
except KeyboardInterrupt:
    led.value(0)