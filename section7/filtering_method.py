import pandas as pd

data = pd.read_csv("pandas_1/chicago.csv").dropna(how = "all")
mask = data["Position Title"].str.lower().str.contains("water")  ###  ye water hai ya nhi ye check krega
mask = data["Position Title"].str.lower().str.startswith("water") ### starting me water hai ya nhi ye check kregaa
mask = data["Position Title"].str.lower().str.endswith("its")       ### end  me its hai ya nhi ye check kregaa
print(mask)