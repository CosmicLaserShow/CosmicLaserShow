import numpy 
import time
import mc
from matplotlib import pyplot as plt

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
        xi, yi = mc.random_coordinate(), mc.random_coordinate()
        list_xi.append(xi)
        list_yi.append(yi)
        plt.scatter(list_xi,list_yi)
        fig.canvas.draw()
        time.sleep(0.01)
    except KeyboardInterrupt:
        break
