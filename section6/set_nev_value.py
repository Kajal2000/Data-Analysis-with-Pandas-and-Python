import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
data1 = data.loc["Dr. No", "Actor"]
data2 = data.loc["Dr. No", "Actor"] = "kajal"  #actor ke gazha pe kajal ho jaayegaa 
data2 = data.loc["Dr. No", [" Box Office","Budget","Bond Actor Salary"]] = [444444, 55555,666]  # DR NO ki column ki value ko chnage kr diya
# print(data2)
# print(data)


# Set multiple value 82
data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
actor_data = data["Actor"] == "Sean Connery"
print(actor_data)