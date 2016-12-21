import numpy 
import time
from matplotlib import pyplot as plt

import mc
import minimizer
import datastructures

fig = plt.figure(figsize=(16,16))

# draw and show it
fig.canvas.draw()
plt.show(block=False)

# data lists
list_xi = []
list_yi = []

start = time.time()
firstTime = True
# loop to update the data
while True:
    try:
        # reset data after x sec
        if (numpy.fmod((time.time() - start),16.0) > 15) and not firstTime:
            print 'reset data'
            start = time.time()
            plt.clf()
            list_xi = []
            list_yi = []
        # get MC pulses and fit for hit (x,y)
        mcdata = mc.generate()
        pulses = [datastructures.Pulse(i,mcdata[i]) for i in range(len(mcdata))]
        hit = datastructures.Hit(pulses)
        minimizer.HitMinimizer(hit)
        # add fitted hit
        list_xi.append(hit.x)
        list_yi.append(hit.y)
        # plot
        plt.scatter(list_xi,list_yi)
        fig.canvas.draw()
        time.sleep(0.01)
        firstTime = False
    except KeyboardInterrupt:
        break
