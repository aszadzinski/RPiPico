from machine import Pin, ADC
from utime import sleep
import math



def set_led(pin,value):
    led = Pin(pin, Pin.OUT)
    led.value(value)
    
def blink(pin, time=0.2,n=1):
    for i in range(n):
        set_led(pin,1)
        sleep(time)
        set_led(pin,0)
        sleep(time)
        

