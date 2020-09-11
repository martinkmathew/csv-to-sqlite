import sqlite3
import os

import pandas as pd

from pandas import DataFrame

filename_withtype = input("enter file name with format") #file name with.csv extension

filename=os.path.splitext(filename_withtype)[0] #splitting the .csv extension
conn = sqlite3.connect(filename+'.sqlite')
c = conn.cursor()

loadfile= pd.read_csv (r'C:\Users\justi\Desktop\nba.csv') #file is saved in desktop folder or specify the file path
loadfile.to_sql(filename, conn, if_exists='append', index = False)

df = DataFrame(c.fetchall(), columns=['Date','Start (ET)','Visitor/Neutral','PTS','Home/Neutral	','PTS.1','Unnamed: 6','Unnamed: 7','Attend.','Notes']) #mentioning the coloumn names

print("file converted successfully ")
