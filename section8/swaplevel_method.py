import pandas as pd 

data = pd.read_csv("pandas_1/bigmac.csv", parse_dates= ["Date"],index_col=["Date","Country"])
data1 = data.sort_index(inplace = True)

swape_data = data.swaplevel()   ## date ke gazha pe country ko kar degaa 
# print(swape_data)
swape_data1 = data.swaplevel("Date","Country") 
swape_data2 = data.swaplevel("Country","Date") 
swape_data2 = data.swaplevel(1,0)
data = data.swaplevel(1,0)                  ## it will overwrite to the orginal in data
print(data)