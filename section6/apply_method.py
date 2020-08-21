import pandas as pd

data = pd.read_csv("pandas_1/jamesbond.csv",index_col = "Film")
data.sort_index(inplace = True)

def convert_to_srting(number):
    return str(number) + "kajal"
    columns = ["Box Office","Budget"]
    for i in columns:
        data[i] = data[i].apply(convert_to_srting)
