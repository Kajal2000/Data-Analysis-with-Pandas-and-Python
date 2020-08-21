import pandas as pd

nba_data = pd.read_csv("pandas_1/nba.csv")
# print(nba_data)
# a = nba_data[["Name","Team","Number"]]
a = nba_data[["Team","Name"]]
print(a)


