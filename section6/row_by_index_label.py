import pandas as pd

a = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
a.sort_index(inplace = True)           # sorted film column 
bond = a.loc["Goldfinger"]            # flim wale row ka pura data de degaa
bond1 = a.loc["Goldfinger" : "Live and Let Die"]   # iss movie se leakr end movie tk ka data milgaa
bond2 = a.loc["Goldfinger":]                      # iss movie ke baas jitna bhi movie h sab ka data mil jaayegaa
print(bond2)