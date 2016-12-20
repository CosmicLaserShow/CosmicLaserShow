#Driver dummy class to mimic data acquisition
#Two flavors:
#1) Data Acq driver. Gives a list of Pulses
#2) Laser grid driver. Accepts a list of Lights to light

from globals import *
from datastructures import *
import mc
import random

class DataAcquisition:

    def getPulses():
        pulses = []
        #Create pulses at random from 'mc' generator        
        npulses = randint(0,2) #0,1 or 2 pulse quartets
        times = []
        for i in range(npulses): 
            times = mc.generate()
            for i in len(times):
                time = times[i]
                pulses.append(Pulse(i,time))
        return pulses
