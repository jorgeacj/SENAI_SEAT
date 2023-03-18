from machine import Pin
from time import sleep

IN1 = Pin(14, Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(32, Pin.OUT)
IN4 = Pin(33, Pin.OUT)

mode = 1 # FULL-STEP = 0 | HALF-STEP = 1
drct = 0 # CW = 0 | CCW = 1

step = 0.001

IN1.value(0)
IN2.value(0)
IN3.value(0)
IN4.value(0)

try:
    while True:
        if mode == 0:
            if drct == 0:
                #STATE 1
                IN4.value(1)
                sleep(step)
                IN4.value(0)
                #STATE 2
                IN3.value(1)
                sleep(step)
                IN3.value(0)
                #STATE 3
                IN2.value(1)
                sleep(step)
                IN2.value(0)
                #STATE 4
                IN1.value(1)
                sleep(step)
                IN1.value(0)
            elif drct == 1:
                #STATE 1
                IN1.value(1)
                sleep(step)
                IN1.value(0)
                #STATE 2
                IN2.value(1)
                sleep(step)
                IN2.value(0)
                #STATE 3
                IN3.value(1)
                sleep(step)
                IN3.value(0)
                #STATE 4
                IN4.value(1)
                sleep(step)
                IN4.value(0)
            else:
                print("ERROR")
        elif mode == 1:
            if drct == 0:
                #STATE 0
                IN1.value(0)
                IN4.value(1)
                sleep(step)
                #STATE 1
                IN3.value(1)
                sleep(step)
                #STATE 2
                IN4.value(0)
                sleep(step)
                #STATE 3
                IN2.value(1)
                sleep(step)
                #STATE 4
                IN3.value(0)
                sleep(step)
                #STATE 5
                IN1.value(1)
                sleep(step)
                #STATE 6
                IN2.value(0)
                sleep(step)
                #STATE 7
                IN4.value(1)
                IN1.value(1)
            elif drct == 1:
                #STATE 0
                IN1.value(1)
                IN4.value(0)
                sleep(step)
                #STATE 1
                IN2.value(1)
                sleep(step)
                #STATE 2
                IN1.value(0)
                sleep(step)
                #STATE 3
                IN3.value(1)
                sleep(step)
                #STATE 4
                IN2.value(0)
                sleep(step)
                #STATE 5
                IN4.value(1)
                sleep(step)
                #STATE 6
                IN3.value(0)
                sleep(step)
                #STATE 7
                IN1.value(1)
                IN4.value(1)
            else:
                print("ERROR")
except KeyboardInterrupt:
    print("Exit")