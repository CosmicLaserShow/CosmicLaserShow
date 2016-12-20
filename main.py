from globals import *
import lasershow, hitconverter

runtime = 10*SECOND #Run for 10 seconds, nice test
show = lasershow.CosmicLaserShow()
converter = hitconverter.HitConverter(show)
show.mainLoop(runtime)

print("Successfully executed")
