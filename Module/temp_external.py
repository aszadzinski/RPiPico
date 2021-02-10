from machine import ADC
from utime import sleep
import math

def get_temperature(pin=27):
    temp_sensor = ADC(pin)
    conv_factor = 3.3/65535
    r0 = 100000.0
    B = 4275.0
    temp = float(temp_sensor.read_u16()*conv_factor)
    vol = temp
    print(temp_sensor.read_u16())
    print(temp)
    r = 1023/temp-1
    r = r0*r
    temp = 1/(math.log(r/r0)/B+(1/298.15))-273.15
    a = 0.029411764705882353
    b = -23.529411764705884
    temp2 = a*temp_sensor.read_u16()*conv_factor*1000 + b
    


    return  (temp2, int(vol*1000))

