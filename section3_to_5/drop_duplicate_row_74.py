
import pandas as pd

df = pd.read_csv("pandas_1/employees.csv")
# a = (df.drop_duplicates())
a = (df.drop_duplicates(subset = ["First Name"]))
b = (df.drop_duplicates(subset = ["First Name"],keep = "first"))     #starting se duplicate dekhegaa
b = (df.drop_duplicates(subset = ["First Name"],keep = "last"))     # last se duplicate dekhegaa
# print(b)


# Uniqu value =======================================================================================
b = (df["Team"].unique())
print(b)