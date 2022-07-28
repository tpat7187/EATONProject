import pandas as pd
import os 


def main():
  path = "dataset/AdvertisingData.xls"
  df = pd.read_excel(path)
  df = df.drop(columns = ['Downloads', 'Watchtime', 'Destination URL', 'Hosting URL'])
  df.to_csv("dataset/Advertising.csv", index=False)



if __name__ == '__main__':
  main()
