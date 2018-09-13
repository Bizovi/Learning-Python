import pandas as pd
import numpy as np
import sqlite3
import openpyxl

def read_data(query):
    """
     Adaugati o noua coloana la dataframe care sa fie compusa din first_name concat cu last name numita
     full name si salvati rezultatul intr-un excel. Apoi pe acest dataframe pentru coloana
     number_of_login calculati mean si standard variation.
    """
    with sqlite3.connect('db.sqlite3') as conn:
        df = pd.read_sql(query,  conn)

    df['Full_Name'] = df['first_name'] + " " + df['last_name']
    return df

if __name__ == "__main__":
    df = read_data('select * from showuser_userscustom')
    df.to_excel("users.xlsx") # write to excel
    print(df.head())

    # mean and sd
    print("The average number of logins is: ", np.mean(df['logins']))
    print("The standard deviation of logins is: ", np.std(df['logins']))