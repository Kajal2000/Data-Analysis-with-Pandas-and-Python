
import pandas as pd

df = pd.read_csv("pandas_1/employees.csv")
# mask = df["Team"].isnull()
# print(df[mask])

mask = df["Team"]
a = mask.sort_index()

print(a)
