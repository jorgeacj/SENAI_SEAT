from machine import Pin, PWM, ADC, Timer
from time import sleep, sleep_us

class Servo(object):
    def __init__(self,pin,angle):
        self.__pwm = Pin(pin, Pin.OUT)
        self.__pulse = int (mapi(angle, 0, 180, 600, 2400))
        tim0= Timer(0)
        tim0.init(period=20, mode=Timer.PERIODIC, callback=lambda t: servo_callback())
    
    def Angle(self, angle = 90):
        self.__pulse = int(mapi(angle, 0, 180, 600, 2400))
        print(self.__pulse)
        pass
    
    def Start(self):
        self.__pwm.value(1)
    
    def Stop(self):
        self.__pwm.value(0)
        
    def mapi_Servo(self, i, i_min, i_max, o_min, o_max):
        return (i - i_min) * (o_max - o_min) / (i_max - i_min) + o_min
    
def servo_callback():
    Servo.Start()
    sleep_us(Servo.__pulse)
    Servo.Stop()
    print("x")
        
Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)

def mapi(i, i_min, i_max, o_min, o_max):
    return (i - i_min)*(o_max - o_min)/(i_max - i_min) + o_min

servo = Servo(12, 90)
try:
    while True:
        ldr_value = Pot.read()
        print(ldr_value)
        angle = mapi(ldr_value, 0, 4095, 0, 180)
        print(angle)
        servo.Angle(angle)
        sleep(1)
except KeyboardInterrupt:
    print("FIM")