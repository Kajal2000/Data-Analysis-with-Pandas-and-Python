import pandas as pd 

f = ["apple","banana","papaya","greap"]
weekday = ["monday","tuesday","wednesday","thusday"]

# print(pd.Series(f,weekday))
# print(pd.Series(data = f, index = weekday))
# print(pd.Series(f, index= weekday))
# print(pd.Series(data = f, index= weekday))

print(pd.Series(data = weekday, index= f))



