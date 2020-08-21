import pandas as pd

a = ["a","b","c","d","e"]
b = pd.Series(a)
print(b)

a = [1,2,3,4,5,6,6]
b = pd.Series(a)
# print(b)

a = [True,False,False]
b = pd.Series(a)
# print(b)