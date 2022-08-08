import pandas as pd
import os 


def main():
  path = "dataset/AdvertisingData.xls"
  df = pd.read_excel(path)
  df = df.drop(columns = ['Downloads', 'Watchtime', 'Destination URL', 'Hosting URL', 'Placement_ID', 'Engagement'])
  df['Year'] = pd.DatetimeIndex(df['Week']).year
  df['Month'] = pd.DatetimeIndex(df['Week']).month
  df['Num_Week'] = pd.DatetimeIndex(df['Week']).weekofyear
  df["BuyingBasis"].replace('instance', 'Instance', inplace = True)
  df["Publication"].replace('Programmatic buying', 'Programmatic Buying', inplace = True)
  df["AdType"].replace('Social email ', 'Social email', inplace = True)
  # filling null values for engagement and impressions
  df['Impressions'] = df['Impressions'].fillna(0) 
  df.to_csv("dataset/Advertising.csv", index=False)

if __name__ == '__main__':
  main()
