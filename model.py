import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

import pandas as pd
import numpy as np
import seaborn as sns
import os 


#dataparser
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')


df = pd.read_csv("dataset/Advertising.csv", low_memory = False, usecols = lambda c: not c.startswith('Unnamed:'), parse_dates=['Week'])


#making a dataframe of only google ad data
row_idx = []
for x in range(len(df)):
  if df.loc[x, 'AdType'] == 'Google Ad Words':
    row_idx.append(x)

google_df = df.loc[row_idx]
#print(google_df)
google_df['year'] =  pd.DatetimeIndex(google_df['Week']).year

#looking at dates year-month-day
#df['year'] = pd.DatetimeIndex(df['Week']).year
#print(df)


# TODO: look at engaements per year by week ? -> by ad type
list_idx = []
list_idx2 = []
null_list = []

for x in range(len(df)): 
  if df.loc[x, 'Week'].year == 2016:
    list_idx.append(x)
  if df.loc[x, 'Week'].year == 2017:
    list_idx2.append(x)
  if df.loc[x, 'Week'].year == 2018: 
    null_list.append(x)

print(null_list)

print(len(list_idx), len(list_idx2))
first_year = df.loc[list_idx]
second_year = df.loc[list_idx2]
third_year = df.loc[null_list]

#all ad types in 2017 are used in 2016 
print(second_year.columns == first_year.columns)
print(third_year.AdType.unique())
print(len(second_year) + len(first_year), len(df))

# if you want to look at the graph
'''
print(segments, df.Segment.nunique())
print('Publications', publications)
'''








