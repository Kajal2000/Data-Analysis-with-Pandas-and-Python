import pandas as pd

nba_data = pd.read_csv("pandas_1/revenue.csv")
# a = nba_data.sum(axis = "columns")    column wise sum krke degaa
# print(a)

#  select one column from data frame

nba_data = pd.read_csv("pandas_1/nba.csv")
# a = nba_data  
# a = nba_data.Name 
# a = nba_data.Team  
# print(a)