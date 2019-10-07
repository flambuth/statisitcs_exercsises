#Gonna setup some stuff I find myself doing repeatedly.
import pandas as pd
import numpy as np
from env import host, user, password

def make_dice_rolls(n_trials, n_dice, make_df=False):
    rolls = np.random.choice(list(range(1,7)), n_trials*n_dice)
    rolls = rolls.reshape((n_trials, n_dice)) 
    return rolls


def get_db_url(username, hostname, password, database):
    """Returns a string that is formatted correctly to access the database """
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

def make_df_from_db(url, table):
    """Returns a dataframe that is made from one table in a database"""
    return pd.read_sql(f'SELECT * FROM {table}', url)
    

# url = get_db_url(user, host, password, db)
# emps_df = pd.read_sql('SELECT * FROM employees', url)
# salary_df = pd.read_sql('SELECT * FROM salaries', url)