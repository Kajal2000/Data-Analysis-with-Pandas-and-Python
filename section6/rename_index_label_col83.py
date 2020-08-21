import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
bond = data.rename(mapper={"GoldenEye" : "kajalSharma"},axis = 0)    # goldname row ko chnage kr degaa kajal naam se 
bond = data.rename(mapper={"GoldenEye" : "kajalSharma", "You Only Live Twice":"Ravvviiiiii"})  # change kr degaa
bond = data.rename(columns = {"Year":"NewYear","Actor":"AAAAAAA"}) #COLUMN NAME CHNAGE KR SKTE HO
bond = data.columns = ["year of", "Actor", "cost", "kajal","sarary","movie_name"]
print(data)