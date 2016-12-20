from globals import *


class Hit:
    def __init__(self,pulselist_):
        this.pulses = pulselist_
        this.x = 0.
        this.y = 0.
        this.time = 0.
        this.chiSquared = 0.

    def setCoords(self,x_,y_,time_,chiSquared_):
        this.x = x_
        this.y = y_
        this.time = time_
        this.chiSquared = chiSquared_

class Pulse:
    def __init__(self,id_,time_):
        this.id = id_
        this.time = time_

class Light:
    def __init__(self,x_,y_,time_):
        this.x = x_
        this.y = y_
        this.time = time_
