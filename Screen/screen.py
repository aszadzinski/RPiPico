from machine import Pin
from utime import sleep,time

class DigitScreen():
    def __init__(self):

        self.digits = [14, 17, 16, 15]
        self.segments = [12,18,13,20,19,21,10,11]
        self.refresh_rate = 0.001
        self.num = {' ':(1,1,1,1,1,1,1,1),
                   '0':(0,0,0,0,0,1,0,1),
                   '1':(1,1,0,1,1,1,0,1),
                   '2':(0,1,0,0,0,1,1,0),
                   '3':(0,1,0,1,0,1,0,0),
                   '4':(1,0,0,1,1,1,0,0),
                   '5':(0,0,1,1,0,1,0,0),
                   '6':(0,0,1,0,0,1,0,0),
                   '7':(0,1,0,1,1,1,0,1),
                   '8':(0,0,0,0,0,1,0,0),
                   '9':(0,0,0,1,0,1,0,0),
                   'C':(0,0,1,0,0,1,1,1),
                   'c':(0,0,1,0,0,0,1,1),
                    '-':(1,1,1,1,1,1,1,0),
                    'H':(1,0,0,0,1,1,0,0),
                    'L':(1,0,1,0,0,1,1,1),
                    'A':(0,0,0,0,1,1,0,0),
                    'B':(1,0,1,0,0,1,0,0),
                    'D':(1,1,0,0,0,1,0,0),
                    'E':(0,0,1,0,0,1,1,0),
                    'F':(0,0,1,0,1,1,1,0),
                    'G':(0,0,1,0,0,1,0,1),
                    'I':(1,0,1,0,1,1,1,1),
                    'J':(1,0,1,0,1,0,1,1),
                    'K':(1,0,1,0,1,1,1,0),
                    'M':(1,1,1,0,1,1,0,0),
                    'N':(1,1,1,0,1,0,0,0),
                    'O':(0,0,0,0,0,1,0,1),
                    'Q':(0,0,0,0,0,0,0,1),
                    'P':(0,0,0,0,1,1,1,0),
                    'R':(0,0,0,0,1,1,0,0),
                    'S':(0,0,1,1,0,1,0,0),
                    'T':(0,0,1,0,1,1,1,1),
                    'U':(1,0,0,0,0,1,0,1),
                    'W':(1,0,0,0,0,1,0,1),
                    'X':(1,0,1,1,0,1,1,1),
                    'Y':(1,0,0,1,1,1,0,0),
                    'Z':(0,1,1,1,0,1,1,1),
                    '_':(1,1,1,1,0,1,1,1),}

        self._digits = []
        self._segments = []
        self.init_digits()
        self.init_segments()
    def init_digits(self):
        for digit in self.digits:
            tmp = Pin(digit, Pin.OUT)
            tmp.value(0)
            self._digits.append(tmp)
            
    def init_segments(self):            
        for segment in self.segments:
            tmp = Pin(segment, Pin.OUT)
            tmp.value(1)
            self._segments.append(tmp)
    def reset_digits(self):
        for digit in self._digits:
            digit.value(0)
            sleep(self.refresh_rate)
            
    def reset_segments(self):            
        for segment in self._segments:
            segment.value(1)
            
    def show(self,_num, t=5, f=0.1):
        _time_start = time()
        #print(_time_start)
        while time()-_time_start < t:
            self.print_num(_num)
                     
    def print_num(self, _num):
        if len(_num) != 4:
            n = 4 - len(_num)
            for i in range(n):
                _num = ' ' + _num
        for digit in range(4):
            self._digits[digit].value(1)
            self.set_num(_num[digit])
            sleep(self.refresh_rate)
            self.reset_digits()
            self.reset_segments()
        return None
                                           
    def set_num(self, _num):
        for i,seg in enumerate(self._segments):
            seg.value(self.num[_num][i])

def test():
    test = DigitScreen()
    test.show('-HC_')
    test.show('1234')
    test.show('2137')

