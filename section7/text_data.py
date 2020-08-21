import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv")
a = data.info()
a = data.nunique()

# b = data["Department"].astype("category")
b = data["Department"].nunique()
# a = data.info()
print(b)