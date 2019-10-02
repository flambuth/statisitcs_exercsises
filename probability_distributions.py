#I don't know much about computers. 
#The simulation methods will start 1-6, after the distrubtion methods 1-6.


import numpy as np
from scipy import stats
np.random.seed(123)


# 1
# A bank found that the average number of cars waiting during the noon hour at 
# a drive-up window follows a Poisson distribution with a mean of 2 cars. Make 
# a chart of this distribution and answer these questions concerning the 
# probability of cars waiting at the drive-up window.
cars_at_noon = stats.poisson(2)

# What is the probability that no cars drive up in the noon hour?
cars_at_noon.pmf(0)

# What is the probability that 3 or more cars come through the drive through?
cars_at_noon.sf(3)

# How likely is it that the drive through gets at least 1 car?
cars_at_noon.sf(1)

# 2
# Grades of State University graduates are normally distributed with a mean of 
# 3.0 and a standard deviation of .3. Calculate the following:

stateU_grades = stats.norm(3.0, .3)

# What grade point average is required to be in the top 5% of the graduating 
# class?
stateU_grades.isf(.05)

# An eccentric alumnus left scholarship money for students in the third decile 
# from the bottom of their class. Determine the range of the third decile. 

#Third decile from teh bottom is 20-30% of students.
stateU_grades.ppf(.20)
stateU_grades.ppf(.30)

print(f"The range of grades within the third decile from the bottoms is {stateU_grades.ppf(.20)} - {stateU_grades.ppf(.30)}.")

# Would a student with a 2.8 grade point average qualify for this scholarship?
stateU_grades.ppf(.20) < 2.8 < stateU_grades.ppf(.30)

# 3
# A marketing website has an average click-through rate of 2%. One day they 
# observe 4326 visitors and 97 click-throughs. 

clicks = stats.binom(4326, .02)

# How likely is it that this many people or more click through?
clicks.sf(97)


# 4
# You are working on some statistics homework consisting of 100 questions where 
# all of the answers are a probability rounded to the hundreths place. Looking 
# to save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?
round_error_distro = stats.binom(60, .01)
round_error_distro.sf(1)


#Well its gonna be a .sf() method to answers, since its asking for a "at least one" answer. Which
#is another way of saying greater than or equal to a value.


# 5
# The codeup staff tends to get upset when the student break area is 
# not cleaned up. Suppose that there's a 3% chance that any one student cleans 
# the break area when they visit it, and, on any given day,    

#about 90% of the 3 active cohorts of 22 students visit the break area.
dailystudents = 3*22*.9

student_cleaning_distro = stats.binom(dailystudents, .03)

# How likely is it that the break area gets cleaned up each day?
#about 60 students per day at .03 chance a piece. So one or more means it got cleaned up.
chance_clean_per_day = student_cleaning_distro.sf(1)

# How likely is it that it goes two days without getting cleaned up?
chance_dirty_per_day = 1 - chance_clean_per_day
    # Permutation of two consecutive days of no cleaning.
chance_dirty_per_day * chance_dirty_per_day
# All week?
    # Permutation of seven consecutive days with a .48 chance of staying dirty.
chance_clean_per_day**7

# 6
# You want to get lunch at La Panaderia, but notice that the line is usually very 
# long at lunchtime. After several weeks of careful observation, you notice that 

# the average number of people in line when your lunch break starts is normally 
# distributed with a mean of 15 and standard deviation of 3. 
lunchline_distro = stats.norm(15,3)

#turning the 15 people into 30 minutes. Maybe 40, since it will always have ten minutes of food prep.
lunchline_distro = stats.norm(40, 3)

# If it takes 2 minutes for each person to order, and 10 minutes from ordering to 
# getting your food, 
#Maybe multiply each person by 2, since you'll have to wait 2 minutes per person in line
#Then add 10 to that value from the distribution.

# what is the likelihood that you have at least 15 minutes left to eat your food 
# before you have to go back to class? Assume you have one hour for lunch, and 
# ignore travel time to and from La Panaderia.
lunchline_distro.cdf(45)




##############
# 1
# A bank found that the average number of cars waiting during the noon hour at 
# a drive-up window follows a Poisson distribution with a mean of 2 cars. Make 
# a chart of this distribution and answer these questions concerning the 
# probability of cars waiting at the drive-up window.