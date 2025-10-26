##PART 3##
###1
#What link is there between life expectancy and income?
#How does the amount of ohysicians affect life expectancy?
#Relationship between women in parliament and level of female tertiary education?

###2
import pandas as pd
import seaborn as sns
data=pd.read_csv("wdi_wide.csv")

###3
info=data.info()
#How many empty values for for Physicians and Population?
#Physicians= 217-207= 10 null entries
#Population= 217-217= 0 null entries

###4
unique_values=print(data.nunique())

###5
description=print(data.describe())
#This output provides us with a total of each colomn, its mean, standard deviation, minimum, Q1, Q2, Q3, and maximum

###6
data["GNI per capita"]=(data["GNI"]/data["Population"]).round(2)
print(data["GNI per capita"])

###7
#How many countries in each region?
countries_per_region=data["Region"].value_counts()
print(countries_per_region)
#Africa:54, Asia:50, Europe:47, Americas:46, Oceania:19

#How many high income economies are there?
high_income=data["High Income Economy"].value_counts()
print(high_income)
#There are 67 high income economies

###8 
#Where are the high income economies?
print(pd.crosstab(data["High Income Economy"], data["Region"]))
#The high income economies are in Europe

###9
filtered_data=data[data["Life expectancy, female"]>80]
#How many countries there are where women can expect to live for more than 80 years? 
print(filtered_data["Country Name"].nunique())
#There are 66 countries where women can expect to live for more than 80 years 
#And which countries those are?
print(filtered_data["Country Name"].tolist())
#'Albania', 'Australia', 'Austria', 'Barbados', 'Belgium', 'Bermuda', 'Canada', 'Cayman Islands', 'Channel Islands', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'France', 'Germany', 'Greece', 'Guam', 'Hong Kong SAR, China', 'Iceland', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Japan', 'Korea, Rep.', 'Lebanon', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Maldives', 'Malta', 'Netherlands', 'New Caledonia', 'New Zealand', 'Norway', 'Oman', 'Panama', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'San Marino', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Spain', 'Sri Lanka', 'St. Martin (French part)', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States', 'Uruguay', 'Virgin Islands (U.S.)'

##PART 4##