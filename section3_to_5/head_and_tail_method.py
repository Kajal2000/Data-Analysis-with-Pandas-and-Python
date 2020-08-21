import pandas as pd 

# head method 
pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# print(pokemon1)
b = pokemon1.head(4)
# print(b)

# tail method
pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
# print(pokemon1)
b = pokemon1.tail(4)
print(b)
