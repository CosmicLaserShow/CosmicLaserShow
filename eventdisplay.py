import numpy 
import time
from matplotlib import pyplot as plt

import mc
import minimizer
import datastructures

fig = plt.figure()

# draw and show it
fig.canvas.draw()
plt.show(block=False)

# data lists
list_xi = []
list_yi = []

# loop to update the data
while True:
    try:
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
        time.sleep(10.01)
    except KeyboardInterrupt:
        break
