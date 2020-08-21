import pandas as pd


food_data = pd.read_csv("pandas_1/foods.csv")
a = food_data.pivot_table(values = "Spend", index = "Gender",aggfunc = "sum")   ##isme Gender column me kitna male or kitna female hai
a = food_data.pivot_table(values = "Spend", index = "Gender",aggfunc = "count")
a = food_data.pivot_table(values = "Spend", index = "Gender",aggfunc = "max")

a = food_data.pivot_table(values = "Spend", index = "Gender",aggfunc = "min")
print(a)



