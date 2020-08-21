import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv")
a = data["Department"].astype("category")

b = data["Name"].str.lower().str.upper()
print(b)

b = data["Name"].str.title()
# # print(b)
main_data = data["Position Title"].str.title()
a = data["Department"].str.len()
# all_data = (data[["Name","Position Title","Department","Employee Annual Salary"].str.title()])
# print(all_data)

