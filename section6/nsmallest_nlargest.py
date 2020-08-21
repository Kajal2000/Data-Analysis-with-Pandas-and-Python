import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)
a = data.nlargest(3,columns = "Box Office")        # box offlice columns me se largesest number dega
b = data.nsmallest(n = 2, columns = "Box Office")    # box offlice columns me se smallest number dega
# print(b)


###### where method ###
a = data.where(data["Box Office"] > 800)    ## 800 hundered se bada hoga wo rahegaa or jo bada nhi h wo nan ho jaayegaa
print(a)