import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv").dropna(how = "all")
data["Department"] = data["Department"].astype("category")
# a = data["Name"]
a = data["Name"].str.split(",", expand = True)   ## alag alag column me data dega
a = data[["First name","last name"]] = data["Name"].str.split(",", expand = True)    ## it will add new comun first name or last name after that split value dono column me chala jaayegaa
# print(data)