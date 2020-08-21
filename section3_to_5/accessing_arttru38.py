import pandas as pd 

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# print(pokemon1.values)
# print(pokemon1.index)


pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# print(pokemon1.values)
# print(index)
# print(pokemon1.dtype)
# print(pokemon1.is_unique)
b = pokemon1.ndim
c = pokemon1.shape
d = pokemon1.size
e = pokemon1.name
print(e)