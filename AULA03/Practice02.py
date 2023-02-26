from time import sleep
from machine import Pin, ADC

led = Pin(2,Pin.OUT)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

try:
    while True:
        ldr_value = ldr.read()
        if ldr_value >= 2000:
            led.value(1)
        else:
            led.value(0)
        print("ADC: ", ldr_value)
        sleep(0.1)
except:
    led.value(0)