import numpy as np
from scipy import stats
die_distro = stats.randint(1,7)

    # What is the probability of rolling a 1?
die_distro.pmf(1) 
    # There's a 1 in 2 chance that I'll roll higher than what number?
die_distro.isf(1/2)
    # What is the probability of rolling less than or equal to 2?
die_distro.cdf(2)
    # There's a 5 in 6 chance that my roll will be less than or equal to what number?
die_distro.ppf(5/6)
    # There's a 1 in 2 chance that my roll will be less than or equal to what number?
die_distro.ppf(1/2)
    # What is the probability of rolling less than or equal to 6?
die_distro.cdf(6)
    # There's a 1 in 3 chance that I'll roll higher than what number?
die_distro.isf(1/3)
    # What is the probability of rolling higher than a 1?
die_distro.sf(1)
    # There's a 2 in 3 chance that my roll will be less than or equal to what number?
die_distro.ppf(2/3)
    # There's a 2 in 3 chance that I'll roll higher than what number?
die_distro.isf(2/3)
    # There's a 1 in 3 chance that my roll will be less than or equal to what number?
die_distro.ppf(1/3)
    # There's a 1 in 6 chance that I'll roll higher than what number?
die_distro.isf(1/6)