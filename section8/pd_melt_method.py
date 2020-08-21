import pandas as pd


data = pd.read_csv("pandas_1/quarters.csv")
# print(data)

a = data.melt()
a = pd.melt(data, id_vars = "Salesman")
a = pd.melt(data, id_vars = "Salesman", var_name = "quarter", value_name = "Revenue")

print(a)

