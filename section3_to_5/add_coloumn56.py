import pandas as pd

nba_data = pd.read_csv("pandas_1/nba.csv")
# print(nba_data)
a = nba_data["kajal"] = "sharma"  
# print(nba_data)                    key value banana kr column add kr diya 

# a = nba_data.insert(3, column = "navg",value = "student")     particular column ke me jaa kr add kregaa 
# print(nba_data)
 

#  BroadCasting Operations
# nba_data = pd.read_csv("pandas_1/nba.csv")            ==      age wale value me 5 add kr degaa jaise 26 age h or 5 add kr diya = 31
b = nba_data["Age"].add(5)
b = nba_data["Age"].sub(5)                              
                                                        # == - kar diya subtracksun kar diya pure me se age wale column se
b = nba_data["Age"].mul(2)   
                                                       # age wale column ki sab value me ko multiply kr diya
b = nba_data["Age"].div(2)                              age wale column ki sab value me ko divide kr diya

print(b)
