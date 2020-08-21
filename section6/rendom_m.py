import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
a = data.sample()             # it will give random data
a = data.sample(n = 5)        # it will give 5 random data
a = data.sample(n = 3,axis = "index") 
a = data.sample(n = 3,axis = "columns") 
print(a) 