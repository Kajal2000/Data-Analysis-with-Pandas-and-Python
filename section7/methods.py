import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv").dropna(how = "all")
chicago_data = data["Name"].str.rstrip().str.lstrip()   ## right or left side se space remove kregaa
chicago_data = data["Name"].str.strip()                  ## dono side se remove kregaa space ko