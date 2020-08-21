import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)

bond = data.query('Actor == "Sean Connery"')   ### Actor wale column se jo bhi sean connery milta hoga wahi return kregaa
# print(bond)
bond = data.query("Budget > 41.9") 
print(bond)