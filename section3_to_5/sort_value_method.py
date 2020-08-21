import pandas as pd 

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
a = pokemon1.sort_values().head()

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# a = pokemon1.sort_values().head()
# a = pokemon1.sort_values(ascending= True)
a = pokemon1.sort_values(ascending= False)

print(a)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
pokemon1 = pd.read_csv("pandas_1/pokemon.csv", index_col = ["Pokemon"],squeeze= True)
a = pokemon1[0]
# print(a)
