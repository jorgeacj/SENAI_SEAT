from machine import Pin, ADC, PWM
from time import sleep

#DEFINES
ldr_left_lux_min = 4000
ldr_rightlux_min = 4000
servo_min = 30
servo_max = 122

#PERIPHERALS
ldr_left = ADC(Pin(35))
ldr_left.atten(ADC.ATTN_11DB)

ldr_right = ADC(Pin(34))
ldr_right.atten(ADC.ATTN_11DB)

servo = PWM(Pin(5), freq=50, duty=0)

#FUNCTIONS
def mapi(i, i_min, i_max, o_min, o_max):
    return (i - i_min)*(o_max - o_min)/(i_max - i_min) + o_min

#MAIN LOOP
try:
    while True:
        v1 = ldr_left.read()
        v2 = ldr_right.read()
        dc = mapi(v1-v2, -ldr_left_lux_min, ldr_rightlux_min, servo_max, servo_min)
        servo.duty(int(dc))
except KeyboardInterrupt:
    print("Exit")