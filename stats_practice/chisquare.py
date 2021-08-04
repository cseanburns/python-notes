import numpy
from scipy.stats import chisquare

# Save as variables as arrays
regions_per = numpy.array([.53, .32, .08, .05, .02])
regions_pro = numpy.array([399, 193, 63, 82, 13])

from scipy.stats import chisquare
data = numpy.array([regions_pro, regions_per])
