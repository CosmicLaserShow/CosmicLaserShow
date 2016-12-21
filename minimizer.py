import globals
import numpy
import scipy
from scipy.optimize import minimize

def chisquared(vars, alignm, data, eps_data = None):
    if not eps_data:
        eps_data = len(data)*[1.0]
    hit = numpy.array([vars[0],vars[1]])
    sum_array = [ ((data[i] - numpy.sqrt((hit - alignm[i]).dot(hit-alignm[i])))/eps_data[i])**2 for i in range(len(data)) ]
    return sum(sum_array)

def HitMinimizer(hit, hit_errors = None, start_hit = [globals.LENGTH * 0.5, globals.LENGTH * 0.5]):
    tlist = hit.pulses
    r_var_list = [ globals.SPEED * t for t in tlist ]
    if not hit_errors:
        hit_errors = len(tlist) * [ 0.5 * globals.NS ]
    r_err_list = [ globals.SPEED * t for t in hit_errors ]
    vars = [start_hit[0], start_hit[1]]
    align = [numpy.array([pmt[0],pmt[1]]) for pmt in globals.PMT_COORDS]
    output = minimize(chisquared, vars, args=(align, r_var_list, r_err_list))
    return output
