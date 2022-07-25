import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

import pandas as pd
import numpy as np
import seaborn as sns
import os 

path = "dataset/AdvertisingData.xls"
df = pd.read_excel(path)
df.to_csv("dataset/Advertising.csv", index=False)
test = pd.read_csv("dataset/Advertising.csv")

print(test)

sns.relplot(x="Impressions", y = "Clicks", data = test)
plt.show()












