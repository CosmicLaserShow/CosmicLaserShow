#Driver dummy class to mimic data acquisition
#Two flavors:
#1) Data Acq driver. Gives a list of Pulses
#2) Laser grid driver. Accepts a list of Lights to light

from globals import *
from datastructures import *
import numpy
import mc
import random
from matplotlib import pyplot as plt

class DataAcquisition:
    def __init__(self):
        self.elapsed = 0

    def getPulses(self):
        pulses = []
        #Create pulses at random from 'mc' generator        
        npulses = random.randint(0,3) #0,1,2 or 3 pulse quartets
        times = []
        for i in range(npulses): 
            times = mc.generate()
            offset = random.randint(50,150) * (i+1)
            for j in range(len(times)): 
                time = times[j] + self.elapsed + offset
                pulses.append(Pulse(j,time))

        self.elapsed += 1*SECOND
        return pulses


class LaserGrid:
    def __init__(self):
        self.fig = plt.figure()
        self.fig.canvas.draw()
        self.xs = []
        self.ys = []

    def reset(self):
        self.xs = []
        self.ys = []

    def activate(self,light):
        self.xs.append(light.x)
        self.ys.append(light.y)

    def showGrid(self):
        plt.scatter(self.xs,self.ys)
        print(self.xs)
        print(self.ys)
        self.fig.canvas.draw()

