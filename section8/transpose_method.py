import pandas as pd 

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)

# print("---------------------------------------------------")
a = data.transpose()                ## interchnage krte h rows ko column me or column ko rows me
# a = data.loc[("Price in US Dollars",)]
print(a)