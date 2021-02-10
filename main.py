import screen
import temp_internal
import temp_external
from utime import sleep
from light import get_light
from led import blink
import _thread

screen = screen.DigitScreen()

while True:
    screen.show("{}C".format(int(temp_internal.get_temperature())), t= 3)
    screen.show("{}c".format(int(temp_external.get_temperature(27)[0])),t=3)
    screen.show("L{}".format(int(get_light(28))),t=3)
    screen.show("{}".format(int(temp_external.get_temperature(27)[1])),t=3)
    _thread.start_new_thread(blink,(25,0.1,3))
    
    