from machine import ADC

def get_light(pin=26):
    temp2_sensor = ADC(pin)
    light = ADC(26)
    conv_factor = 3.3/65535

    lux = light.read_u16()*conv_factor/2*100
    return int(lux)
