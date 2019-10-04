#I don't know much about computers. 
#The simulation methods will start 1-6, after the distrubtion methods 1-6.

import pandas as pd
import numpy as np
from scipy import stats
from env import host, user, password
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
cars_at_noon.sf(2)

# How likely is it that the drive through gets at least 1 car?
cars_at_noon.sf(0)

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

# If I have a GPA of 3.5, what percentile am I in?
stateU_grades.cdf(3.5)

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
round_error_distro.sf(0)


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
chance_clean_per_day = student_cleaning_distro.sf(0)

# How likely is it that it goes two days without getting cleaned up?
chance_dirty_per_day = 1 - chance_clean_per_day
    # Permutation of two consecutive days of no cleaning.
chance_dirty_per_day * chance_dirty_per_day
# All week?
    # Permutation of seven consecutive days with a .48 chance of staying dirty.
chance_dirty_per_day**7

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


# 7
# Connect to the employees database and find the average salary of current 
# employees, along with the standard deviation. Model the distribution of 
# employees salaries with a normal distribution and answer the following 
# questions:

db = 'employees'
def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

url = get_db_url(user, host, password, db)
emps_df = pd.read_sql('SELECT * FROM employees', url)
salary_df = pd.read_sql('SELECT * FROM salaries', url)

#Find mean() and stdev() of the column in salary_df
salary_mean = salary_df['salary'].mean()
salary_std = salary_df['salary'].std()

salary_distro = stats.norm(salary_mean, salary_std)
salary_distro.cdf()

# What percent of employees earn less than 60,000?
salary_distro.cdf(60000)

# What percent of employees earn more than 95,000?
salary_distro.sf(95000)

# What percent of employees earn between 65,000 and 80,000?
salary_distro.cdf(80000)-salary_distro.cdf(65000)

# What do the top 5% of employees make?
salary_distro.isf(.05)












##############
# 1
# A bank found that the average number of cars waiting during the noon hour at 
# a drive-up window follows a Poisson distribution with a mean of 2 cars. Make 
# a chart of this distribution and answer these questions concerning the 
# probability of cars waiting at the drive-up window.
n_tests = 1000


x = np.random.poisson(2,n_tests)
#
#  What is the probability that no cars drive up in the noon hour?
(x == 0).sum()/len(x)

# What is the probability that 3 or more cars come through the drive through?
(x > 2).sum()/len(x)

# How likely is it that the drive through gets at least 1 car?
(x > 0).sum()/len(x)

# 2
# Grades of State University graduates are normally distributed with a mean of 3.0 and 
# a standard deviation of .3. 
mu = 3.0
sdev = .3
n_trials = 1000
grades = np.random.normal(3.0, .3, n_trials)
# Calculate the following:
# What grade point average is required to be in the top 5% of the graduating class?
np.percentile(grades, 95)
# # What GPA constitutes the bottom 15% of the class?
np.percentile(grades, 15)
# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their 
# class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify 
# for this scholarship?
np.percentile(grades, 20)
np.percentile(grades, 30)

print(f"The range of grades within the third decile from the bottoms is {np.percentile(grades, 20)} thru {np.percentile(grades, 30)}.")

# If I have a GPA of 3.5, what percentile am I in?
#Find the amount of grades in the trial set that is above 3.5. The mean function divides that sum by the n_trials
#Subtract that from 1, since you want to find what percentile was less than this. So it'd be 96th percentile.
1 - (grades > 3.5).mean()


# 3
# A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 
# click-throughs. How likely is it that this many people or more click through?
n_tests = 50
customers = np.random.random((n_tests, 4326))
sample_clickrate = 97/4326

customers < sample_clickrate

#This is a 1D array of that is n_trials long. It element is how many clicks happened in the trial.
simulated_clicks = (customers < sample_clickrate).sum(axis=1)
simulated_clicks.mean()
simulated_clicks.std()

sim_clicks_distro = stats.norm(simulated_clicks.mean(), simulated_clicks.std())
sim_clicks_distro.sf(97)

# 4
# You are working on some statistics homework consisting of 100 questions where all of the answers 
# are a probability rounded to the hundreths place. Looking to save time, you put down random 
# probabilities as the answer to each question.

n_tests = 1000

#1000 trials with 60 questions each. 
homework_trials = np.random.random((n_tests, 60))

# What is the probability that at least one of your first 60 answers is correct?

#
(homework_trials<=.01).sum(axis=1).mean()
#Which is .599. 
#Different than my other method. Don't know why.


# 5
# The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that 
# there's a 3% chance that any one student cleans the break area when they visit it, and, on any 
# given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it 
# that the break area gets cleaned up each day? How likely is it that it goes two days without 
# getting cleaned up? All week?
n_trials = 1000
cleaning_trials = np.random.random(n_trials, 90)

#This sees if there are any randos that came up less than .03 in each trial of 90 students. Counts the
#trials that had at least one True.
per_day_clean_chance = (np.any(cleaning_trials<.03, axis=1)).mean()

# How likely is it that it goes two days without getting cleaned up?
(1-per_day_clean_chance) ** 2

# All week?
(1-per_day_clean_chance) ** 7

# 6
# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, you notice that the average number of people in line 
# when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, 
# what is the likelihood that you have at least 15 minutes left to eat your food before you have to go 
# back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
n_trials = 1000
#I forgot to double the st dev, since i doubled the measurement of 1people==2minutes
#adding the 10 minutes for waiting for the order ought to be handled outside the normal curve generation
lunchline_trials = np.random.norm(30, 6, n_trials)

#The greater than statement should be greater than longst possible time.
#45 minutes, - 10 for the food prep time

(lunchline_trials<35).mean()

# 7
# Connect to the employees database and find the average salary of current employees, along with the 
# standard deviation. Model the distribution of employees salaries with a normal distribution and 
# answer the following questions:

#I think I'll make a normal curve with the mu and sigma from what I find from the theoretical
#work I already did for this exercise.

salary_mean=63810.744836143705
salary_std=16904.831259952276

salary_randos = np.random.normal(salary_mean, salary_std, 1000)

# What percent of employees earn less than 60,000?
(salary_randos<60000).mean()
# What percent of employees earn more than 95,000?
(salary_randos>95000).mean()
# What percent of employees earn between 65,000 and 80,000?
((salary_randos<80000).sum() - (salary_randos>65000).sum())/len(salary_randos)
# What do the top 5% of employees make?
np.percentile(salary_randos, 95)