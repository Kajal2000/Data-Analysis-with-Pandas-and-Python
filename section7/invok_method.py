import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv", index_col= "Name").dropna(how = "all")
data.index = data.index.str.strip().str.title()
# print(data)
cha = data.columns.str.upper()  ## sare column name upper case me ho jaayega
print(cha)