import pandas as pd 

nba_data = pd.read_csv("pandas_1/nba.csv")   
a = nba_data.sort_values("Age",ascending = False)   
                                                    # Ascending false means bada se chota
a = nba_data.sort_values("Name",ascending = False)    # Ascending false means z se jo naam hoga wo phele aayegaa z,x,y

b = nba_data.sort_values("Age",ascending = True)  

df = nba_data.sort_values(by = ["Age","Number"], ascending =[True,False])
print(df)                     