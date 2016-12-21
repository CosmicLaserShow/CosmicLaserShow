from globals import *
from datastructures import *
from minimizer import *

class HitConverter: 
    def __init__(self):
        self.pmts = len(PMT_COORDS)
        print(self.pmts)
        self.stream = []
        self.processed = []	
        self.hits = []

    def reset(self):
        self.hits = []

    def processPulses(self):
        toProcess = []
        hasIds = [False] * self.pmts
        for pulse in self.stream:
            toProcess.append(pulse)
            hasIds[pulse.id] = True
       
        #Can we create a hit from all the pulses we have so far?
        if hasIds == [True] * self.pmts:
            processed_pulses = self.__checkForHit(toProcess)
            for pulse in processed_pulses: 
                self.stream.remove(pulse) #Once a pulse is used it's no longer needed
        return self.hits

    def __checkForHit(self, toProcess):
        #Simple but ugly solution implemented (for now):
        #1) Pick the first t0,t1,....tn
        #2) accept this as the 'hit'
        #3) Remove these from the list
        #4) If possible to make another hit, go to 1
        #5) Computed hits in list, processed pulses in list
        #6) Send hits to steering, pulses are returned 

        processed_pulses = []
        valid_hits = []
        while len(toProcess) >= self.pmts:
            successes = [False for _ in range(self.pmts)]
            processed_thisround = [None for _ in range(self.pmts)]

            GPSTime = -1
            Nano = -1

            for pulse in toProcess:
                id = pulse.id
                if successes[id] == True: continue
                if GPSTime > 0 and not pulse.GPSTime == GPSTime: continue
                if Nano > 0 and not abs(pulse.Nano - Nano) < 6: continue

                successes[id] = True
                processed_thisround[id] = pulse
                if successes == [True] * self.pmts: break
            
            if successes == [True] * self.pmts:
                hit = Hit(processed_thisround)
                HitMinimizer(hit)
                print("x= %1.2f y= %1.2f t= %1.2f chisq=%.2f" % (hit.x,hit.y,hit.time,hit.chiSquared))
                if self.__isValid(hit): valid_hits.append(hit)
            
            #Discard either all pulses of hit or pulses of an incomplete hit	
            processed_pulses += processed_thisround
            for pulse in processed_thisround:
                toProcess.remove(pulse)
            
            #we will now try again with the remaining pulses               
        
        self.hits = valid_hits  
        return processed_pulses

    def __isValid(self, hit):
        #TODO: Actual code here
        return True

    def addPulses(self, pulses):
        self.stream += pulses
  
    def addPulse(self, pulse):
        self.stream.append(pulse)
