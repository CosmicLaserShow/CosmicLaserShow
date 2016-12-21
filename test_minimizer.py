import math
import minimizer
import datastructures
import mc
import globals

# mc test
mcdata = mc.generate()
print mcdata

# test
start_hit = [globals.LENGTH/4.0, globals.LENGTH/4.0]

fac = math.sqrt(2.0) * 0.5 * globals.LENGTH / globals.SPEED

meas_time = [ fac * 1.05, fac * 0.95, fac * 0.9, fac * 1.1] 
meas_errs = len(meas_time) * [ fac * 0.1 ]
meas_puls = [datastructures.Pulse(i,mcdata[i]) for i in range(len(mcdata))]
meas_hit  = datastructures.Hit(meas_puls)

output = minimizer.HitMinimizer(meas_hit) #, meas_errs, start_hit)

x   = output.x
cov = output.hess_inv

print 'fit results:'
print 'x_start = %.5f; x = %.5f +/- %.5f' % (round(start_hit[0],5),round(x[0],5),round(math.sqrt(cov[0][0]),5))
print 'y_start = %.5f; y = %.5f +/- %.5f' % (round(start_hit[1],5),round(x[1],5),round(math.sqrt(cov[1][1]),5))
print 'chisquared = %.1f' % (round(output.fun,5))
