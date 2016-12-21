import math
import minimizer
import datastructures
import mc
import globals

# mc test
mcdata = mc.generate()
print(mcdata)

# test
start_hit = [globals.LENGTH/4.0, globals.LENGTH/4.0]

#fac = math.sqrt(2.0) * 0.5 * globals.LENGTH / globals.SPEED

#meas_time = [ fac * 1.05, fac * 0.95, fac * 0.9, fac * 1.1] 
#meas_errs = len(meas_time) * [ fac * 0.1 ]
meas_puls = [datastructures.Pulse(i,mcdata[i]) for i in range(len(mcdata))]
meas_hit  = datastructures.Hit(meas_puls)

minimizer.HitMinimizer(meas_hit) #, meas_errs, start_hit)

print('fit results:')
print('x_start = %.5f; x = %.5f +/- %.5f' % (round(start_hit[0],5),round(meas_hit.x,5),round(meas_hit.x_err,5)))
print('y_start = %.5f; y = %.5f +/- %.5f' % (round(start_hit[1],5),round(meas_hit.y,5),round(meas_hit.y_err,5)))
print('chisquared = %.1f' % (round(meas_hit.chiSquared,5)))
print('average arrival time from fitted point is %.5f +/- %.5f' % (round(meas_hit.time,5),round(meas_hit.time_err,5)))
