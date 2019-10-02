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
#Driving by 2 billboards on one million occasions
n_tests = 1000000
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

#That is pretty close to what the online binomial calculator i used.
print(f"The probability of seeing two data science students on both billboards is {exactly_2.sum()/n_tests}%.")


# 4
# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending 
# machine. If on monday the machine is restocked with 17 poptart packages, how likely is it 
# that I will be able to buy some poptarts on Friday afternoon?

#Makes 1D array with 5 observations, each chosen randomly between 3 and 4.5
def find_friday_poptarts(n_trials):
    #makes an array, each element is a (1,5) array. 
    trials = np.asarray([np.random.randint(low = 1, high = 6, size = 5) for i in range(n_trials)])
    #find the sum of those four elements and subtract it from 17.
    friday = trials.sum(axis=1) - 17
    #These are the trials that have one cookie available friday morning.
    return f"There is a {(friday >= 1).sum()/n_trials}% chance there will be 1 cookie on Friday afternoon."

# 5 Compare Heights

# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?

def find_chance_of_woman_larger_than_man(n_trials):
    #The height numbers for men and women
    male_mu, male_sigma = 178, 8                                                     
    female_mu, female_sigma = 170, 6 
    #Make a big random set of each sex
    males = np.random.normal(male_mu, male_sigma, n_trials)
    females = np.random.normal(female_mu, female_sigma, n_trials)
    #Return the boolean masked outcome of female being larger than a male. The sum is 
    #the trials where the woman was larger. 
    return ((females > males).sum())/n_trials 


# 6
# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download 
# is corrupted and the installation fails. What are the odds that after having 50 students 
# download anaconda, no one has an installation issue? 100 students?
p_corrupt = float(1/250)


#Set the table. Terms are how many trials we'll simulate. How many hosts will be installed and
#have a chance to be corrupt, at the rate of 1 out of 250 will be.
n_trials = 1000 
n_hosts = 50 
p_corruption = 1/250 

#Generate the n_trials, each a nparray of 50, which is how many hosts got conda installed. So 1000x50  
installs = np.random.random((n_trials, n_hosts))   

#evaluate which of these random values are less than 0.004, the 1/250 translated to decimal
#The sum of each row is collapsed into one value, which is the sum of the "Trues" in the row.
(installs < p_corruption).sum(axis=1)
#This is the rows that had no corrupt installs. So divide that by the n_tests and that is 
#the percentage of 50 hosts installs that had zero corruption.
no_corruption = ((installs < p_corruption).sum(axis=1) == 0).sum()
no_corruption/n_trials

def find_no_corruption_chance(n_trials, n_hosts, p_corrupt=1/250):
    installs = np.random.random((n_trials, n_hosts)) 
    no_corruption = ((installs < p_corruption).sum(axis=1) == 0).sum()
    return no_corruption/n_trials

find_no_corruption_chance(1000, 50)
find_no_corruption_chance(1000, 100)

# What is the probability that we observe an installation issue within the first 150 students 
# that download anaconda?

def find_one_corrupt_chance(n_trials, n_hosts, p_corrupt=1/250):
    installs = np.random.random((n_trials, n_hosts)) 
    no_corruption = ((installs < p_corruption).sum(axis=1) >= 1).sum()
    return no_corruption/n_trials

find_one_corrupt_chance(1000, 150)

# How likely is it that 450 students all download anaconda without an issue?
find_one_corrupt_chance(1000,450)

# 7
# There's a 70% chance on any given day that there will be at least one food truck at Travis 
# Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# How likely is it that a food truck will show up sometime this week?

#Set the table:
n_trials = 1000 
n_days = 7 
p_truck = .7

#Find likelihood for first 3 days, at .3 a piece, all having no food trucsk

#Make the random array. Trials are rows, each row has 7 days/column/fields
weekdays = np.random.random((n_trials, n_days))   
weekdays < .3

#This is the first 3 columns of each trials
first3 = weekdays[:,[0,1,2]]
#Of those first3days on each trial, now many had 3 trues?
no_truck_on_first3 = ((first3 < p_truck).sum(axis=1) == 3).sum()
no_truck_on_first3/n_trials

def find_chance_of_truck(n_trials, n_days, p_truck=.7)
    weekdays = np.random.random((n_trials, n_days))
    truck_shows_up = ((weekdays < p_truck).sum(axis=1) >= 1).sum()
    return truck_shows_up/n_trials

#There are four days left in the week. What are the chances any of those 4 days has a truck day?
find_chance_of_truck(1000,4)

# 8
# 23 people are in the same room, what are the odds that two of them share a birthday? 
# What if it's 20 people? 40?

#Lets rephrase that into some terms to put on the table:
# Calculate the probability of generating a duplicate random number after
# generating "n" random numbers in the range "d"

n_trials=1000
n_people=23
days_in_the_year = list(range(1,366))
birthdays = np.random.choice(days_in_the_year, 23)

def generate_birthdays(n_people):
    return np.random.choice(days_in_the_year, n_people)

#lets make a lot of sets of 23 birthdays

x = [generate_birthdays() for i in range(n_trials+1) ]

#This counts the length of each row. I should make a function that counts uniques

def count_uniques(nparray):
    return len(np.unique(nparray))


z = np.apply_along_axis(count_uniques,1,x)
#This is the sum of all the trials that had some non-unique numbers 
(z < 23).sum()

#Lets make it a function!
def find_birthday_paradox_chance(n_trials, n_people):
    days_in_the_year = list(range(1,366))
    def generate_birthdays(n_people):
        return np.random.choice(days_in_the_year, n_people)
    x = [generate_birthdays(n_people) for i in range(n_trials) ]
    def count_uniques(nparray):
        return len(np.unique(nparray))
    z = np.apply_along_axis(count_uniques,1,x)
    return ((z < n_people).sum())/n_trials
#I don't think it works. It everything above 90 is a 100%. oh well. I came close!