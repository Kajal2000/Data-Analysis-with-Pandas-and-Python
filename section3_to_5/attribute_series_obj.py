import pandas as pd 

a = [1,2,3,4,5,6,6]
b = pd.Series(a)
# print(b)

#  for sum method 
a = [1,2,3,4,5,6,6]
b = pd.Series(a)
c = b.sum()
# print(c)

# //   unique value 
a = [1,2,3,4,5,6,6]
b = pd.Series(a)
c = b.unique()
print(c)