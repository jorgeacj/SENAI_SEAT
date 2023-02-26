from machine import Pin, time_pulse_us
from time import sleep
from utime import sleep_us

#Ultrassom
trig = Pin(21, Pin.OUT)
echo = Pin(22, Pin.IN)
#Dmax = 500 cm, D = t/58, timeout = 500x58 = 29000
timeout = 29000

def ultrassom_tempo():
  #Pulso de 10us
  trig.value(0)
  sleep_us(2) 
  trig.value(1)
  sleep_us(10) 
  trig.value(0)
  #Mede o tempo do pulso
  pulse_time = time_pulse_us(echo, 1, timeout)
  return pulse_time

def ultrassom_cm(tempo_us):
  return (0.172146 * tempo_us - 0.86406) / 10 

while True:
  tempo = ultrassom_tempo()
  distancia = ultrassom_cm(tempo)
  print("Tempo (us) = ", tempo)
  print("Distância (cm) = ", distancia)
  sleep(0.3)

while False:
  tempo = ultrassom_tempo()
  dist_mm = 0.01715*tempo
  dist_calibrada = 1.00*dist_mm + 0.00
  #dist_calibrada = 1.00*tempo + 0.00
  print("Tempo (us) = ", tempo)
  print("Distância (cm) = ", dist_mm)
  print("Distância calibrada (cm) = ", dist_calibrada)
  sleep(0.3)

