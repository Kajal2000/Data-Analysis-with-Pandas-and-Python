import pandas as pd 

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", index_col = ["Pokemon"],squeeze= True)
a = pokemon1.head(3)
a = pokemon1.apply()

print(a)