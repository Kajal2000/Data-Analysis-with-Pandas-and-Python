import pandas as pd

a = pd.read_csv("pandas_1/jamesbond.csv")
b = a.set_index(keys = "Film")                          # index ke gazha pe flim ka data aayegaa index hat jaayegaa            
c = a.set_index(keys = "Film", inplace = True)          # will not get output 
reset_data = a.reset_index()                            # reset means orginal data will return 

reset_data1 = a.reset_index(drop = True)                # flim wala column ko remove kr degaa
reset_data2 = a.reset_index(drop = False)               # flim column wapis aa jaayegaa
print(reset_data2)