#What happened to propellerheads? They had that one really good album.
import numpy as np
import pandas as pd


# 1

# How likely is it that you roll doubles when rolling two dice?
n_trials = 1000
n_dice = 2
#Make an array of random choices of 1-6. It is as big as the total number of dice being rolled
#which is 2 dice per trial, at 1000 trials. 2000 dice rolling outcomes
rolls = np.random.choice(list(range(1,7)), n_trials*n_dice)                                                                  
#Making the array break of at pairs of 2, representing a trial of 2 die being rolled.
rolls = rolls.reshape(n_trials,n_dice)
#Shifted into a data frame so that I can compare one column with another
df = pd.DataFrame(rolls) 
#Boolean mask that evaluates who has matching column values
df[0] == df[1]
#The length of the df with only the doubles making it through the mask
doubles = len(df[df[0] == df[1]])
#So dividing that value by the n_trials is the likelhood of doubles
doubles/n_trials

# 2
# If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the 
# probability of getting more than 3 heads?
n_flips = 100
n_coins = 8
flips = np.random.choice(['heads','tails'], n_flips*n_coins)
#Make a bunch of 8 coines per flip trials. Each are a row.
flips = flips.reshape(n_flips, n_coins)
#Evaluates everything in the np array. So each row is 8 true or falses
head_flips = flips == 'heads'
#Count the Trues
head_flips.sum(axis=1)
#From that one dimensional array, you can skim out the 3's or => 2's to answer the question
exactly_3 = (head_flips.sum(axis=1) == 3).sum()
atleast_3 = (head_flips.sum(axis=1) > 2).sum()

print(f"The chances of getting exactly 3 heads out of 8 coins is {exactly_3/len(head_flips)}%.")
print(f"The chances of getting exactly 3 heads out of 8 coins is {atleast_3/len(head_flips)}%.")

# 3
# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that 
# the two billboards I drive past both have data science students on them?

#Set the amount of trials to run. There are 2 billboards and a 1:3 ratio of data to web
#                                                              25:75, or 1 in 4
n_tests = 100
n_billboards = 2
p_data = .25

#Generate a 100 trials.
billboards = np.random.random((n_tests, n_billboards))               
#Skim out the ones that were less than the chances of picking a data scientist out of all
#codeup students
#This array is a 1D array, that is n_tests long. Each true is a row that had two Trues,
#meaning there was 2 data students in the trial
exactly_2 = (billboards < p_data).sum(axis=1) == 2).sum()
#sum them up to see how many, and then divide it by the n_trials
exactly_2.sum()/n_tests

print(f"The probability of seeing two data science students on both billboards is {exactly_2.sum()/n_tests}%.")