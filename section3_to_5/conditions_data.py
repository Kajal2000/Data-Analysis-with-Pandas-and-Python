import pandas as pd

nba_data = pd.read_csv("pandas_1/employees.csv")
# print(nba_data["Gender"])                              # only Gender column return kregaa
a = nba_data["Gender"] == "Male"                        # True false return kregaa male jaha hoga waha true krega otherwise false
a = nba_data["Bonus %"] < 1.5                            # 1.5 se kaam hoga to false return kregaa

print(a)
