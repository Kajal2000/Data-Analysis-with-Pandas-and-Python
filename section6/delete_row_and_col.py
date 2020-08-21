import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
a = data.drop("A View to a Kill")  ### row ki value ko remove kr dega
a = data.drop(["A View to a Kill","Skyfall"]) ### multiple value remove kr skti ho
# print()


##### Remove column ####
a = data.drop("Director",axis = 1)    # Dircector ka column delete kar degaa
a = data.drop("Year",axis = "columns")  
a = data.drop(["Year","Budget","Actor"],axis = "columns") 
b = data.pop("Actor")    # it will remove single series
print(b)