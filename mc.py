import globals
import random

def random_coordinate():
    return random.uniform(0., globals.LENGTH)

def generate():
    x, y = random_coordinate(), random_coordinate()

    result = []
    for pmt in globals.PMT_COORDS:
        d = globals.distance(pmt, (x, y))
        t = d / globals.SPEED
        result.append(t)

    return result
