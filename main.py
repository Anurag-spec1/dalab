# create a dictioary having fields Country,Capital,Population

import pandas as pd

data ={
    "Population":[1000000,2000000,3000000,9000000,69000000,100000000,45000000],
    "Capital":["New Delhi","Washington D.C.","Beijing","Paris","Tokyo","London","Berlin"],
}

countries_df=pd.DataFrame(data,index=["India","USA","China","France","Japan","UK","Germany"])

print(countries_df) 

print(countries_df.head())
print(countries_df.tail())

print(countries_df.loc["India","Population"])

countries_df["GDP"]=[2.87, 21.43, 14.34, 2.71, 5.08, 2.83, 3.86]

print(countries_df)