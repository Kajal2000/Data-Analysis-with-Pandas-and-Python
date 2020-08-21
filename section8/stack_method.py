import pandas as pd 

data = pd.read_csv("pandas_1/worldstats.csv", index_col=["country","year"])
# data1 = data.sort_index(inplace = True)
# print(data)
# print("---------------------------------------")
a = data.stack()   ## column name it's transform itsa row level
a = data.stack().to_frame()
# print(a)


