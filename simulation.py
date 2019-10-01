#What happened to propellerheads? They had that one really good album.
import numpy as np
import pandas as pd
import fredstats as fstats


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
