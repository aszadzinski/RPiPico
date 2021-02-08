import screen
import temp_internal
from utime import sleep
from light import get_light

screen = screen.DigitScreen()

while True:
    screen.show("{}C".format(int(temp_internal.get_temperature())), t= 5)
    screen.show("_{}".format(int(get_light())),t=3)
    