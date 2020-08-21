import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv").dropna(how = "all")
a = data["Position Title"]
b = data["Name"].str.split(",").str.get(0)
c = data["Name"].str.split(",").str.get(1)
data2 = data["Name"].str.split(",").str.get(0).str.title().value_counts()
b = data["Name"].str.split(",").str.get(1).str.strip().str.split(" ")
print(b)