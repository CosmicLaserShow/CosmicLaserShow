from globals import *
import sqlite3
import time
import random
import mc
import os

conn = sqlite3.connect(os.path.expanduser("~/cosmics.db"))
c = conn.cursor()
c.execute("CREATE TABLE Hits (GPSTime INT, ID INT, Timing INT, Nanoseconds INT)")

starttime = time.time()
while True:
    time.sleep(0.01)
    if not random.randint(0,3) == 1: continue
    pulses = mc.generate()
    print(pulses)
    gpstime = int( (time.time()-starttime)* 1000)
    for i in range(4):
       timings = pulses[i]
       nano = gpstime*(10**6) + (pulses[i])
       print("Generated: %d, %d, %d, %d" % (gpstime,nano,i,timings) )
       c.execute("INSERT INTO Hits VALUES (?,?,?,?)", (gpstime,nano,i,timings) )
       conn.commit() 

        
