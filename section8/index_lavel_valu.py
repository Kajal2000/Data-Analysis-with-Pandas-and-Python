import pandas as pd

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)
a = data.index.get_level_values("Date")
b = data.index.get_level_values(0)

data1 = data.index.get_level_values("Country")
data1 = data.index.get_level_values(1)
# print(data1)
