import pandas as pd 

nba_data = pd.read_csv("pandas_1/nba.csv")
# a = nba_data["Team"].value_counts()            value ko count krke btayegaa
a = nba_data["Position"].value_counts()  
print(a)
