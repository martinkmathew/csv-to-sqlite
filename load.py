import sqlite3

import pandas as pd

from pandas import DataFrame

filename = input("enter file name")
conn = sqlite3.connect(filename+'.sqlite')
c = conn.cursor()

read_clients = pd.read_csv (r'C:\Users\justi\Desktop\nba.csv')
read_clients.to_sql('nba', conn, if_exists='append', index = False)
df = DataFrame(c.fetchall(), columns=['Date','Start (ET)','Visitor/Neutral','PTS','Home/Neutral	','PTS.1','Unnamed: 6','Unnamed: 7','Attend.','Notes'])

print("file converted successfully ")
