

import pandas as pd

data = pd.read_csv("pandas_1/salesmen.csv",parse_dates=["Date"])

sales = data["Salesman"] = data["Salesman"].astype("category")
# print(sales)

sales = data.pivot(index = "Date", columns = "Salesman",values = "Revenue")  ### column ko convert kr deta h column headers me
print(sales)




