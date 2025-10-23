import pandas as pd
import seaborn as sns
data=pd.read_csv("wdi_wide.csv")

#3
info=data.info()
#How many empty values for for Physicians and Population?
#Physicians= 217-207= 10 null entries
#Population= 217-217= 0 null entries

#4
unique_values=print(data.nunique())

#5
description=print(data.describe())

#6
data["GNI per capita"]=(data["GNI"]/data["Population"]).round(2)
print(round(data["GNI per capita"]))

#7
#How many countries in each region?

#How many high income economies are there?
high_income=pd.value_counts
print(high_income)