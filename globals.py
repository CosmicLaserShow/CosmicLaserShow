import math

MM = 1.
M = 1000 * MM

NS = 1.
S = 10**9 * NS

SPEED_OF_LIGHT = 299792458. * M / S
SPEED = (2./3.) * SPEED_OF_LIGHT

LENGTH = 500. * MM

PMT_COORDS = [(0., 0.), (LENGTH, 0.), (0., LENGTH), (LENGTH, LENGTH)]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

