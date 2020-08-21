import pandas as pd

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)

b = data.index.set_names(names = ["Day","Location"])   ##it will chnage the column name
print(b)