from machine import ADC
from utime import sleep

temp_sensor = ADC(4)
conv_factor = 3.3/65535


def get_temperature():
    reading = temp_sensor.read_u16()*conv_factor
    temp = 25-(reading - 0.706)/0.001721
    #print("temp:{}".format(temp))
    return temp


