from globals import *
from datastructures import *
import lasershow


class HitConverter: 
    def __init__(self, lasershow):
        self.steering = lasershow
        self.stream = []
        self.processed = []	
        self.hits = []

    def processPulses(self, currtime):
        grace_time = 1 * MS
        expiration_time = 100 * MS 

        toProcess = []
        toDelete = []
	
        hasIds = [False, False, False, False]
	
        for pulse in stream:
            too_old = pulse.time - currtime > expiration_time
            if too_old:
                toDelete.append(pulse)
                continue	

            mature =  pulse.time - currtime > grace_time
            if mature: 
                toProcess.append(pulse)
                hasIds[pulse.id] = True
       
        for pulse in toDelete:
            #pulse did not hit all 4 phototubes
            #dont process these. Delete from stream to save computing power
            stream.remove(pulse)            
 
        #Can we create a hit from all the pulses we have so far?
        if hasIds == [True,True,True,True]:
            processed_pulses = __checkForHit(toProcess)
            for pulse in processed_pulses: 
                stream.remove(pulse) #Once a pulse is used it's no longer needed

    def __checkForHit(self, toProcess):
        #Simple but ugly solution implemented (for now):
        #1) Pick the first t0,t1,t2,t3
        #2) accept this as the 'hit'
        #3) Remove these from the list
        #4) If possible to make another hit, go to 1
        #5) Computed hits in list, processed pulses in list
        #6) Send hits to steering, pulses are returned 

        processed_pulses = []
        valid_hits = []
        while len(toProcess) >= 4: #also terminates if more than 4 pulses don't have a valid hit together
            successes = [False,False,False,False]
            processed_thisround = [None,None,None,None]
            for pulse in toProcess:
                id = pulse.id
                if successes[id] == True: continue
                successes[id] = True
                processed_thisround[id] = pulse
                if successes == [True,True,True,True]: break
            
            if successes == [True,True,True,True]:
                hit = Hit(processed_thisround)
                HitMinimizer.compute(hit)
                if __isValid(hit): valid_hits.append(hit)	
                processed_pulses += processed_thisround
                for pulse in processed_thisround:
                    toProcess.remove(pulse)
                #we will now try again with the remaining pulses
            else:
                break #collection of pulses cannot make a valid hit anymore
                
        self.hits = valid_hits  
        return processed_pulses

    def __isValid(self, hit):
        #TODO: Actual code here
        return True

    def addPulses(self, pulses):
        self.stream += pulses
  
    def addPulse(self, pulse):
        self.stream.append(pulse)
