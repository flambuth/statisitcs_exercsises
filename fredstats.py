#Gonna setup some stuff I find myself doing repeatedly.
# import pandas as pd
# import numpy as np

def make_dice_rolls(n_trials, n_dice, make_df=False):
    import numpy as np
    rolls = np.random.choice(list(range(1,7)), n_trials*n_dice)
    rolls = rolls.reshape((n_trials, n_dice)) 
    return rolls