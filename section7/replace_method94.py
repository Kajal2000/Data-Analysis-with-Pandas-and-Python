import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv").dropna(how = "all")  ## NaN value ko remove kr dega
a = data["Department"] = data["Department"].astype("category")
# print(data.tail(3))
a = data["Department"].str.replace("MGMNT","Management")       ## mgmnt ko management me convert kr degaa
a = data["Employee Annual Salary"].str.replace("$","").astype(float) 
print(a)