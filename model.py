import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

import pandas as pd
import numpy as np
import seaborn as sns
import os 

df = pd.read_csv("dataset/Advertising.csv", low_memory = False, usecols = lambda c: not c.startswith('Unnamed:'))

#print(test.axes)
#TODO: How to get dates from date column
#Current Interest: Google Ad Sense (Curret/Exact Matches)



#Uniques: 
ad_types = df.AdType.unique()
segments = df.Segment.unique()
publications = df.Publication.nunique()
treatments = df.Treatment.unique()

#ad types -> ad subtype
#print(ad_types, df.AdType.nunique())
#print(treatments, df.Treatment.nunique())

row_idx = []
for x in range(len(df)):
  if df.loc[x, 'AdType'] == 'Google Ad Words':
    row_idx.append(x)

google_df = df.loc[row_idx]
print(google_df.Region.unique())
#impressions seem to indicate pricing

  

'''
print(segments, df.Segment.nunique())
print('Publications', publications)
'''













