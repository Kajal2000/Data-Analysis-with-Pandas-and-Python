import pandas as pd 


pokemon1 = pd.read_csv("pandas_1/pokemon.csv", usecols= ["Pokemon"],squeeze= True)
print(pokemon1)

pokemon1 = pd.read_csv("pandas_1/google_stock_price.csv")
# print(pokemon1)