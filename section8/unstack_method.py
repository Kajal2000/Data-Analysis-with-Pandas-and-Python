import pandas as pd


## unstack method() ##
data = pd.read_csv("pandas_1/worldstats.csv", index_col=["country","year"])
data2 = data.unstack()
data2 = data.unstack().unstack().unstack()

data3 = data.unstack(0)
data3 = data.unstack(-1)
data3 = data.unstack(level = [1,0])

data3 = data.unstack(level = [0,1])
data3 = data.unstack(level = ["country","year"])
print(data3)