import pandas as pd

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"])
print(data)