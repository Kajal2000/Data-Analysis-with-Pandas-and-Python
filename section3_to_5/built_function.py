import pandas as pd 

pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# print(pokemon1)
a = len(pokemon1)
# print(a)
a = type(pokemon1)
# print(a)
a = list(pokemon1)
# print(a)
a = max(pokemon1)
print(a)


