from machine import Pin, time_pulse_us
from time import sleep
from utime import sleep_us

#DEFINES
PI = 3.141592
R_TANK = 6.2 # in cm
H_TANK = 10.8
BASE = PI*pow(R_TANK,2)

TIMEOUT = 29000

#PERIPHERALS
trig = Pin(21, Pin.OUT)
echo = Pin(22, Pin.IN)

#FUNCTIONS
def us_time():
  trig.value(0)
  sleep_us(2) 
  trig.value(1)
  sleep_us(10) 
  trig.value(0)
  pulse_time = time_pulse_us(echo, 1, TIMEOUT)
  return pulse_time

def us_dist_cm(time_us):
  return (0.0174063 * time_us - 0.3122305)

#MAIN LOOP
try:
    while True:
        time = us_time()
        dist = H_TANK - us_dist_cm(time)
        vol  = BASE * dist
        if vol < 0:
            vol = 0
        print("Volume (cm^3) = ", vol)
        sleep(1)
except KeyboardInterrupt:
    print("Exit")