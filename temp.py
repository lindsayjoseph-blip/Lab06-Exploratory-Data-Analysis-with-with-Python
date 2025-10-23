import pandas as pd
import seaborn as sns
data=pd.read_csv("wdi_wide.csv")
info=data.info()
#How many empty values for for PHysicians and Population?
info=data.info("Physicians")
