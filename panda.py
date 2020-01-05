#!/usr/bin/python3
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 
import pandas as pd ##load panda with pd as the alias

file = r'price.csv'
df = pd.read_csv(file, sep='*', error_bad_lines=False)


print(df)   ##print file
df.columns = ['current', 'open', 'high' , 'low' , 'avg', 'date']  #name columns to call 
#print(df['current'].head())
print('avg:',df['current'][0], 'date', df['date'][0])  ##print 'column' and 'row'
#print('date: ',df['date'][0])