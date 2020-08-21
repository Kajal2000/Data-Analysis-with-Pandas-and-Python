import pandas as pd

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates = ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)

a = data.loc["2010-01-01"]
a = data.loc["2010-01-01","Argentina"]
# a = data.loc[("2010-01-01","Argentina")," Price in US Dollars"]
a = data.loc[("2010-01-01",)]

print(a)