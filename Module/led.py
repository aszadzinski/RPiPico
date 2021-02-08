from machine import Pin, ADC
from time import sleep
import math

led = Pin(25, Pin.OUT)
test = Pin(22,Pin.OUT)
temp_sensor = ADC(4)
temp2_sensor = ADC(27)
light = ADC(26)
conv_factor = 3.3/65535
r0 = 1000
B = 4275

while True:
    led.value(1)
    test.value(0)
    sleep(1)
    led.value(0)
    test.value(1)
    sleep(1)
    temp2 = temp2_sensor.read_u16()*conv_factor
    r = 1023/temp2-1
    r = r0/r
    temp2 = 1/(math.log(r/r0)/B+1/298.15)-274.15
    
    reading = temp_sensor.read_u16()*conv_factor
    temp = 18-(reading - 0.706)/0.001721
    print("temp:{} light:{} temp2:{}".format(temp, light.read_u16(), temp2))

