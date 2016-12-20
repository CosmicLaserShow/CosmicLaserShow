from globals import *

class Hit:

    def __init__(self, pulselist_):
        self.pulselist = pulselist_
	self.x = 0.0
	self.y = 0.0
	self.time = 0.0

    def setCoords(self, time_, x_, y_):
        self.x = x_
        self.y = y_
        self.time = time_

