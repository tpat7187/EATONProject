import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

import pandas as pd
import numpy as np
import seaborn as sns
import os 

path = "dataset/AdvertisingData.xls"
df = pd.read_excel(path)
df = df.drop(columns = ['Downloads', 'Watchtime', 'Destination URL', 'Hosting URL'])
df.to_csv("dataset/Advertising.csv", index=False)
test = pd.read_csv("dataset/Advertising.csv", low_memory = False, usecols = lambda c: not c.startswith('Unnamed:'))


print(test.axes)


#if you want to see the test of the plot
#sns.relplot(x="Impressions", y = "Clicks", data = test)
#plt.show()














