import pandas as pd

df = pd.read_csv("pandas_1/employees.csv")

mark1 = df["Gender"] == "Male"
mark2 = df["Team"] == "Marketing"

# print(df[mark1 & mark2])

# print(df[mark1 & mark2])  
