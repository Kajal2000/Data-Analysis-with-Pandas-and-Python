
import pandas as pd

df = pd.read_csv("pandas_1/employees.csv")
mark1 = df["First Name"] == "Robert"
mark2 = df["Team"] == "Client Services"
mark3 = df["Start Date"]> "2016-06-01"

# print(df[(mark1 & mark2) | mark3]) 
# print(df[mark1 & mark2])  

#  ek column me se bhut sare row ko cheak karwana chahte ho wo isin method use krna hoga

# main1 = df["Team"] == "Legal"
# main2 = df["Team"] == "Sales"
# main3 = df["Team"] == "Product"

a = df["Team"].isin(["Legal","Sales","Product"])
# print(a)