import pandas as pd 

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", index_col = ["Pokemon"],squeeze= True)
# a = pokemon1.head(3)
a = pokemon1.get(0)
a = pokemon1.get("Moltres")
a = pokemon1.get([0,5])
# a = pokemon1.get("Moltres","Meowth")
a = pokemon1.get(key = "dog", default = "not found")
print(a)