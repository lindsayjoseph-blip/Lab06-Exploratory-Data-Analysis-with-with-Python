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

###1
#Is there any association between GNI per capita and life expectancy?
sns.relplot(data, x="GNI per capita", y="Life expectancy, female")
sns.relplot(data, x="GNI per capita", y="Life expectancy, male")
#Yes, positive curve, life expectancy increases rapidly for lower GNI per capita but flattens outs the higher the GNI level is

###2
#Does the association between GNI per capita and life expectancy vary by region?
sns.relplot(data, x="GNI per capita", y="Life expectancy, female", hue="Region")
sns.relplot(data, x="GNI per capita", y="Life expectancy, male", hue="Region")
#Yes

###3
sns.relplot(data, x="GNI per capita", y="Life expectancy, female", hue="Region", kind="line", errorbar="sd")
sns.relplot(data, x="GNI per capita", y="Life expectancy, male", hue="Region", kind="line", errorbar="sd")

#The resaon why we can not see the standard deviation as a line is because it could not be represented through only having one value per item category. 

###4
sns.lmplot(data, x="GNI per capita", y="Life expectancy, female", hue="Region")
sns.lmplot(data, x="GNI per capita", y="Life expectancy, male", hue="Region")

###5
sns.relplot(data, x="Physicians", y="Life expectancy, female")
sns.relplot(data, x="Physicians", y="Life expectancy, male")

gf=sns.FacetGrid(data, col="Region")
gf.map(sns.scatterplot, "Physicians", "Life expectancy, female")
gm=sns.FacetGrid(data, col="Region")
gm.map(sns.scatterplot, "Physicians", "Life expectancy, male")
#Are these relationships similar for male life expectancy? from the graph, The relationships between the life expectancy of male and females in their respective regions in function of the chosen numerical feature (Physician proportion) is indeed similar for each gender. 

#5 more questions:
   #1: How does the relationship of woman in national parliament and females in tertiary education vary from a region to another? 
sns.relplot(data, x="Women in national parliament", y="Tertiary education, female")
g=sns.FacetGrid(data, col="Region")
g.map(sns.scatterplot, "Women in national parliament", "Tertiary education, female")
   #2:How does the relationship between the GNI and the International tourism vary from a region to another? 
sns.relplot(data, x="International tourism", y="GNI", hue="Region", kind="line") 
g=sns.FacetGrid(data, col="Region")
g.map(sns.scatterplot, "International tourism", "GNI")
   #3:How does the relationship between the proportion of physicians and the women in tertiary education vary from a region to another?
sns.relplot(data, x="Physicians", y="Tertiary education, female")
g=sns.FacetGrid(data, col="Region", hue= "Region")
g.map(sns.scatterplot, "Physicians", "Tertiary education, female")
   #4:How does the relationship between the proportion of physicians and the men in tertiary education vary from a region to another? 
sns.relplot(data, x="Physicians", y="Tertiary education, male")
g=sns.FacetGrid(data, col="Region", hue= "Region")
g.map(sns.scatterplot, "Physicians", "Tertiary education, male")  
   #5: Do regions with higher GNI have higher internet use (access to internet)? 
sns.lmplot(data, x="GNI per capita", y="Internet use", hue="Region")
g=sns.FacetGrid(data, col="Region", hue= "Region")
g.map(sns.scatterplot, "GNI per capita", "Internet use")  

###6
#a #Is there any association between Internet use and emissions per capita? 
data["Emissions per capita"]=(data["Greenhouse gas emissions"]/data["Population"])
sns.relplot(data, x="Internet use", y="Emissions per capita")
print(data["Emissions per capita"])

#b #Which are the countries with high emissions? (> 0.03)?
filtered_countries=data[data["Emissions per capita"]>0.03]
print(filtered_countries["Country Name"].tolist())
#'Brunei Darussalam'and 'Qatar'

#c #Is there much variation by region (with respect to high emissions vs Internet use)?
sns.relplot(data, x="Internet use", y="Emissions per capita", hue="Region")

#d #Do all high income economies have high emissions?**********
