#Main Class and entry point of program

#DataAcquistion: Can be called for list of Pulses
#HitConverter: Transfers list of pulses to list of Hits
#HitMinimizer: Gives an individual pulse-based hit to a time,x,y data structure.
#Scheduler: Schedule the hits to be played on the laser board
#LaserGrid: Has knowledge of the 10x10 field of lasers and lights them at will

from globals import *
from datastructures import Light
import time
import hitconverter
import drivers


runtime = 10*SECOND #Run for 10 seconds, nice test
converter = hitconverter.HitConverter()
acquisition = drivers.DataAcquisition()
grid = drivers.LaserGrid()

starting_time = time.time()
ending_time = starting_time + (runtime / SECOND)

expected_runtime = 1 #1 second
cycle_duration = 0
run = 0
while(time.time() < ending_time):
     converter.reset()
     grid.reset()
     run += 1
     sleeptime = expected_runtime - cycle_duration
     time.sleep(sleeptime)

     cycle_starttime = time.time() #Benchmark how long it took (roughly, in ms)
     #ALL THE WORK TO BE DONE IN A CYCLE IS DONE HERE

     print("This is run" + str(run))

     pulses = acquisition.getPulses() #Check all pulses received from data by now
     print("Retrieved %d pulses during this run" % len(pulses))

     converter.addPulses(pulses)  
     hits = converter.processPulses()

     for hit in hits:
         light = Light(hit)
         grid.activate(light)

     grid.showGrid()

     #print(hits)
     #ALL THE WORK TO BE DONE IN A CYCLE ENDS HERE
     cycle_endtime = time.time() #End the benchmark
     cycle_duration = cycle_starttime - cycle_endtime

print("Program successfully executed!")
