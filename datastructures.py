from globals import *


class Hit:
    def __init__(self,pulselist_):
        self.pulses = pulselist_
        self.x = 0.
        self.y = 0.
        self.time = 0.
        self.chiSquared = 0.

    def setCoords(self,x_,y_,time_,chiSquared_):
        self.x = x_
        self.y = y_
        self.time = time_
        self.chiSquared = chiSquared_

class Pulse:
    def __init__(self,id_,time_):
        self.id = id_
        self.time = time_

class Light:
    def __init__(self,x_,y_,time_):
        self.x = x_
        self.y = y_
        self.time = time_
