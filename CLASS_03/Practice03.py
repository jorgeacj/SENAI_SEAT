from machine import Pin, ADC
from time import sleep
import math

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

try:
    while True:
        ldr_value = ldr.read()
        voltage = (ldr_value/4095.0)*3.3
        res = voltage*10000.0/(3.3-voltage)
        lum = 10**(6.5-1.25*math.log(res,10))
        print("LDR Value: ", ldr_value)
        print("Voltage: ", voltage)
        print("Resistance: ", res)
        print("Luminance: ", lum)
        print("")
        sleep(2.0)
except:
    print("FIM")
