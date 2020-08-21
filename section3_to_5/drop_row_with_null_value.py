import pandas as pd 

nba_data = pd.read_csv("pandas_1/nba.csv")   
# a = nba_data.dropna()                           jitna bhi null value hai sab ko remove kr dega row me se
a = nba_data.dropna(how = "all")                  jiska pura column nan hai wahi remove hoga
# a = nba_data.dropna(subset= ["Salary","College"]).head(7)  particular row me se null ko remove kregaa
print(a) 
