import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

import pandas as pd
import numpy as np
import seaborn as sns
import os 



df = pd.read_csv("dataset/Advertising.csv", low_memory = False, usecols = lambda c: not c.startswith('Unnamed:'), parse_dates=['Week'])


# Restarting rn because im sad 0
#print(df.AdType.unique())
test_frame = df.loc[df.AdType == 'Email'].reset_index(drop = True)

# splitting dataset by year

cringe = []
date15, date16, date17, date18 = 0, 0, 0, 0

for x in range(len(df)):
  year = df.loc[x, 'Week'].year
  cringe.append(year)
  if year == 2015:
    date15 += 1
    print(df.loc[x])
  if year == 2016:
    date16 += 1
  if year == 2017:
    date17 += 1
  if year == 2018:
    date18 += 1


print(date15, date16, date17, date18)
#print(set(cringe))

# Could do it by month instead of week it will probably be easier
#print(test_frame.Week.nunique(), len(test_frame))

months = [0]*12

for x in range(len(test_frame)):
  month = test_frame.loc[x, 'Week'].month
  #print(month)
  months[month-1] += test_frame.loc[x, 'Impressions']

print(months)
'''
plt.plot(months)
plt.show()
'''


