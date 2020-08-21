import pandas as pd

a = pd.read_csv("pandas_1/jamesbond.csv")
b = a.iloc[0]                                    # index waise data dega iloc or zero wale index ka pura row ka data dega
b = a.iloc[10:15]                                # 10 se 15 tk ka data degaa
b = a.iloc[0:] 
b = a.iloc[[5,10,15]]                             # only 5 ka deta dega phir 10 ka data degaa phir 15 ka deta degaa
# print(b)


# pacing the second argument 

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
# print(data.loc["Moonraker","Actor"])
# a = data.loc["Moonraker","Director"]
# print(data.loc["Moonraker",["Director","Box Office"]])   # sare ka data degaa
# print(data.loc["Moonraker":"Thunderball","Director":"Budget"]) # Range ke jaisa kaam kregaa
print(data.loc["Moonraker":"Director":])  