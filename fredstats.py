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

# Use the employees database.
url = get_db_url(user,host,password,'employees')

def kevins_query():
    """ Makes 3 Columns that are the difference of days between two date values:
    """
    employees = pd.read_sql('''SELECT
        e.*,
        datediff('2002-09-30', e.hire_date) tenure,
        t.title,
        t.from_date title_from,
        datediff('2002-09-30', t.from_date) t_tenure,
        et.titles,
        s.salary,
        s.from_date salary_from,
        datediff('2002-09-30', s.from_date) s_tenure,
        es.salaries
    FROM
        employees e
    JOIN 
        titles t 
        USING(emp_no)
    JOIN 
        salaries s 
        USING(emp_no)
    JOIN
        (SELECT 
            emp_no,
            count(*) titles
        FROM
            titles
        GROUP BY
            emp_no) et
        USING(emp_no)
    JOIN
        (SELECT 
            emp_no,
            count(*) salaries
        FROM
            salaries
        GROUP BY
            emp_no) es
        USING(emp_no)
    WHERE
        s.to_date > '2002-09-30'
        AND t.to_date > '2002-09-30';
    ''', url)

# Is there a relationship between how long an employee has been with the company and their salary?

# Is there a relationship between how long an employee has been with the company and the number 
# of titles they have had?
