import pandas as pd

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)
a = data.sort_index()
b = data.sort_index(ascending = True)
b = data.sort_index(ascending = False)     ##sab column ko reverse kr degaa
b = data.sort_index(ascending = [True,False])
b = data.sort_index(ascending = [False,True])   ## first column ko reverse kr degaa and second ko acending order me kar degaa
# print(data)
# print("---------------------------------------------------------------")
# print(b)
b = data.sort_index(level = "Country")     ## only country acending order me aayegaa
# print(b)
b = data.sort_index(level = 0)
b = data.sort_index(level = 1)  

b = data.sort_index(level = "Date")
print(b)

