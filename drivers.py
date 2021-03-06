#Driver dummy class to mimic data acquisition
#Two flavors:
#1) Data Acq driver. Gives a list of Pulses
#2) Laser grid driver. Accepts a list of Lights to light

from globals import *
from datastructures import *
import numpy
import mc
import os
import sqlite3
import random
from matplotlib import pyplot as plt

class DataAcquisition:
    def __init__(self):
        self.elapsed = 0
        self.pulselist = []
        
        dbname = os.path.expanduser('CosmicLaserShow.db')
        self.conn = sqlite3.connect(dbname)
        c = self.conn.cursor()
#        c.execute("SELECT * FROM Hits")
#        for row in c:
#           if row[0] > self.elapsed: self.elapsed = row[0]      

    def syncDatabase(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM Hits WHERE GPSTime<%d AND ID<%d" % (self.elapsed,2))
        for row in c:
            #print(row)
            #if row[0] > self.elapsed: self.elapsed = row[0]         
            newpulse = Pulse(row[2],row[3])
            newpulse.setTimings(row[0],row[1])
            self.pulselist.append(newpulse)

    def getPulses(self):
        self.pulselist = []
        self.syncDatabase()
        return self.pulselist

class LaserGrid:
    def __init__(self):
        self.fig = plt.figure()
        plt.show(block=False)
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
        self.fig.canvas.draw()
        somegrid = [[0]*11 for _ in range(11)]
        #print(self.xs)
        #print(self.ys)
        for i in range(len(self.xs)):
           somegrid[self.ys[i]][self.xs[i]] = 1
        for list in somegrid: print(list)



