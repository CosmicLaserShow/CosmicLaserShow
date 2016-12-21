from globals import *
import numpy

class Hit:
    def __init__(self,pulselist_):
        self.pulses = pulselist_
        self.x = 0.
        self.y = 0.
        self.x_err = 0.
        self.y_err = 0.
        self.time = 0.
        self.time_err = 0.
        self.chiSquared = 0.

    def setCoords(self,x_,y_,x_err_,y_err_,time_,time_err_,chiSquared_):
        self.x = x_
        self.y = y_
        self.x_err = x_err_
        self.y_err = y_err_
        self.time = time_
        self.time_err = time_err_
        self.chiSquared = chiSquared_

class Pulse:
    def __init__(self,id_,time_):
        self.id = id_
        self.time = time_
        
        #SQL values for matching  
        self.GPSTime = 0
        self.Nano = 0

    def setTimings(self, t1, t2):
        self.GPSTime = t1
        self.Nano = t2

class Light:
    def __init__(self,hit):
        self.x = int( 10*hit.x / LENGTH)
        self.y = int( 10*hit.y / LENGTH) 

class Track:
    def __init__(self):
        self.x = numpy.array([0.,0.,0.])
        self.u = numpy.array([0.,0.,0.])
        self.x_err = numpy.array([0.,0.,0.])
        self.u_err = numpy.array([0.,0.,0.])
        self.chisquared = 0.

    def setPosition(self,x_,y_,z_):
        self.x = numpy.array([x_,y_,z_])
    
    def setPositionError(self,x_err_,y_err_,z_err_):
        self.x_err = numpy.array([x_err_,y_err_,z_err_])

    def setDirection(self,u_x_,u_y_,u_z_):
        self.u = numpy.array([])

    def setDirectionErr(self,u_x_err_,u_y_err_,u_z_err_):
        self.u_err = numpy.array([u_x_err_,u_y_err_,u_z_err_])

    def setChiSquared(self,chisquared_):
        self.chisquared = chisquared_

