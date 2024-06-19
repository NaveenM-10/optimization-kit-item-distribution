# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:01:03 2024

@author: Naveen
"""

# Pushing the Raw data into Mysql database 
import pandas as pd
data=pd.read_csv(r"C:\Users\Naveen\Desktop\Project_Team_162\KIT.csv")

from sqlalchemy import create_engine

import pymysql

engine=create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                     .format(user = 'root',
                             pw = 'password',
                             db = 'kit'))

data.to_sql('kit_raw_data', con=engine, if_exists='replace', chunksize= None, index= False)

#Importing the Raw data from MySQL
sql='select * from kit_raw_data'

#Trying to load the data from MySQL database
kit=pd.read_sql(sql,engine)

#   EDA Before Data Pre-Processing
# Measures of Central Tendency 
# First moment business decision

#MEAN

kit['Total'].mean()
kit["04-01-2021 00:00"].mean()
kit["05-01-2021 00:00"].mean()
kit["06-01-2021 00:00"].mean()
kit["07-01-2021 00:00"].mean()
kit["08-01-2021 00:00"].mean()
kit["09-01-2021 00:00"].mean()
kit["10-01-2021 00:00"].mean()
kit["11-01-2021 00:00"].mean()
kit["12-01-2021 00:00"].mean()
kit["01-01-2022 00:00"].mean()
kit["02-01-2022 00:00"].mean()
kit["03-01-2022 00:00"].mean()
kit["04-01-2022 00:00"].mean()
kit["05-01-2022 00:00"].mean()
kit["06-01-2022 00:00"].mean()
kit["07-01-2022 00:00"].mean()
kit["08-01-2022 00:00"].mean()
kit["09-01-2022 00:00"].mean()
kit["10-01-2022 00:00"].mean()
kit["11-01-2022 00:00"].mean()
kit["12-01-2022 00:00"].mean()
kit["01-01-2023 00:00"].mean()
kit["02-01-2023 00:00"].mean()
kit["03-01-2023 00:00"].mean()
kit["04-01-2023 00:00"].mean()
kit["05-01-2023 00:00"].mean()
kit["06-01-2023 00:00"].mean()
kit["07-01-2023 00:00"].mean()
kit["08-01-2023 00:00"].mean()
kit["09-01-2023 00:00"].mean()
kit["10-01-2023 00:00"].mean()
kit["11-01-2023 00:00"].mean()
kit["12-01-2023 00:00"].mean()

#MEDIAN
kit['Total'].median()
kit["04-01-2021 00:00"].median()
kit["05-01-2021 00:00"].median()
kit["06-01-2021 00:00"].median()
kit["07-01-2021 00:00"].median()
kit["08-01-2021 00:00"].median()
kit["09-01-2021 00:00"].median()
kit["10-01-2021 00:00"].median()
kit["11-01-2021 00:00"].median()
kit["12-01-2021 00:00"].median()
kit["01-01-2022 00:00"].median()
kit["02-01-2022 00:00"].median()
kit["03-01-2022 00:00"].median()
kit["04-01-2022 00:00"].median()
kit["05-01-2022 00:00"].median()
kit["06-01-2022 00:00"].median()
kit["07-01-2022 00:00"].median()
kit["08-01-2022 00:00"].median()
kit["09-01-2022 00:00"].median()
kit["10-01-2022 00:00"].median()
kit["11-01-2022 00:00"].median()
kit["12-01-2022 00:00"].median()
kit["01-01-2023 00:00"].median()
kit["02-01-2023 00:00"].median()
kit["03-01-2023 00:00"].median()
kit["04-01-2023 00:00"].median()
kit["05-01-2023 00:00"].median()
kit["06-01-2023 00:00"].median()
kit["07-01-2023 00:00"].median()
kit["08-01-2023 00:00"].median()
kit["09-01-2023 00:00"].median()
kit["10-01-2023 00:00"].median()
kit["11-01-2023 00:00"].median()
kit["12-01-2023 00:00"].median()

#MODE
kit['Total'].mode()
kit["Customer Code"].mode()
kit["Customer Name"].mode()
kit["KIT ITEM"].mode()
kit["Product type"].mode()
kit['OEM'].mode()
kit["Item Description"].mode()
kit["Item Code"].mode()
kit["04-01-2021 00:00"].mode()
kit["05-01-2021 00:00"].mode()
kit["06-01-2021 00:00"].mode()
kit["07-01-2021 00:00"].mode()
kit["08-01-2021 00:00"].mode()
kit["09-01-2021 00:00"].mode()
kit["10-01-2021 00:00"].mode()
kit["11-01-2021 00:00"].mode()
kit["12-01-2021 00:00"].mode()
kit["01-01-2022 00:00"].mode()
kit["02-01-2022 00:00"].mode()
kit["03-01-2022 00:00"].mode()
kit["04-01-2022 00:00"].mode()
kit["05-01-2022 00:00"].mode()
kit["06-01-2022 00:00"].mode()
kit["07-01-2022 00:00"].mode()
kit["08-01-2022 00:00"].mode()
kit["09-01-2022 00:00"].mode()
kit["10-01-2022 00:00"].mode()
kit["11-01-2022 00:00"].mode()
kit["12-01-2022 00:00"].mode()
kit["01-01-2023 00:00"].mode()
kit["02-01-2023 00:00"].mode()
kit["03-01-2023 00:00"].mode()
kit["04-01-2023 00:00"].mode()
kit["05-01-2023 00:00"].mode()
kit["06-01-2023 00:00"].mode()
kit["07-01-2023 00:00"].mode()
kit["08-01-2023 00:00"].mode()
kit["09-01-2023 00:00"].mode()
kit["10-01-2023 00:00"].mode()
kit["11-01-2023 00:00"].mode()
kit["12-01-2023 00:00"].mode()

# Measures of Dispersion 
# Second moment business decision

# variance      
kit['Total'].var()
kit["04-01-2021 00:00"].var()
kit["05-01-2021 00:00"].var()
kit["06-01-2021 00:00"].var()
kit["07-01-2021 00:00"].var()
kit["08-01-2021 00:00"].var()
kit["09-01-2021 00:00"].var()
kit["10-01-2021 00:00"].var()
kit["11-01-2021 00:00"].var()
kit["12-01-2021 00:00"].var()
kit["01-01-2022 00:00"].var()
kit["02-01-2022 00:00"].var()
kit["03-01-2022 00:00"].var()
kit["04-01-2022 00:00"].var()
kit["05-01-2022 00:00"].var()
kit["06-01-2022 00:00"].var()
kit["07-01-2022 00:00"].var()
kit["08-01-2022 00:00"].var()
kit["09-01-2022 00:00"].var()
kit["10-01-2022 00:00"].var()
kit["11-01-2022 00:00"].var()
kit["12-01-2022 00:00"].var()
kit["01-01-2023 00:00"].var()
kit["02-01-2023 00:00"].var()
kit["03-01-2023 00:00"].var()
kit["04-01-2023 00:00"].var()
kit["05-01-2023 00:00"].var()
kit["06-01-2023 00:00"].var()
kit["07-01-2023 00:00"].var()
kit["08-01-2023 00:00"].var()
kit["09-01-2023 00:00"].var()
kit["10-01-2023 00:00"].var()
kit["11-01-2023 00:00"].var()
kit["12-01-2023 00:00"].var()

# standard deviation
kit['Total'].std() 
kit["04-01-2021 00:00"].std()
kit["05-01-2021 00:00"].std()
kit["06-01-2021 00:00"].std()
kit["07-01-2021 00:00"].std()
kit["08-01-2021 00:00"].std()
kit["09-01-2021 00:00"].std()
kit["10-01-2021 00:00"].std()
kit["11-01-2021 00:00"].std()
kit["12-01-2021 00:00"].std()
kit["01-01-2022 00:00"].std()
kit["02-01-2022 00:00"].std()
kit["03-01-2022 00:00"].std()
kit["04-01-2022 00:00"].std()
kit["05-01-2022 00:00"].std()
kit["06-01-2022 00:00"].std()
kit["07-01-2022 00:00"].std()
kit["08-01-2022 00:00"].std()
kit["09-01-2022 00:00"].std()
kit["10-01-2022 00:00"].std()
kit["11-01-2022 00:00"].std()
kit["12-01-2022 00:00"].std()
kit["01-01-2023 00:00"].std()
kit["02-01-2023 00:00"].std()
kit["03-01-2023 00:00"].std()
kit["04-01-2023 00:00"].std()
kit["05-01-2023 00:00"].std()
kit["06-01-2023 00:00"].std()
kit["07-01-2023 00:00"].std()
kit["08-01-2023 00:00"].std()
kit["09-01-2023 00:00"].std()
kit["10-01-2023 00:00"].std()
kit["11-01-2023 00:00"].std()
kit["12-01-2023 00:00"].std()

#   RANGE

max(kit['Total']) - min(kit['Total'])
max(kit["04-01-2021 00:00"]) - min(kit["04-01-2021 00:00"]) 
max(kit["05-01-2021 00:00"]) - min(kit["05-01-2021 00:00"]) 
max(kit["06-01-2021 00:00"]) - min(kit["06-01-2021 00:00"]) 
max(kit["07-01-2021 00:00"]) - min(kit["07-01-2021 00:00"])
max(kit["08-01-2021 00:00"]) - min(kit["08-01-2021 00:00"])
max(kit["09-01-2021 00:00"]) - min(kit["09-01-2021 00:00"])
max(kit["10-01-2021 00:00"]) - min(kit["10-01-2021 00:00"]) 
max(kit["11-01-2021 00:00"]) - min(kit["11-01-2021 00:00"]) 
max(kit["12-01-2021 00:00"]) - min(kit["12-01-2021 00:00"]) 
max(kit["01-01-2022 00:00"]) - min(kit["01-01-2022 00:00"]) 
max(kit["02-01-2022 00:00"]) - min(kit["02-01-2022 00:00"]) 
max(kit["03-01-2022 00:00"]) - min(kit["03-01-2022 00:00"]) 
max(kit["04-01-2022 00:00"]) - min(kit["04-01-2022 00:00"])
max(kit["05-01-2022 00:00"]) - min(kit["05-01-2022 00:00"])
max(kit["06-01-2022 00:00"]) - min(kit["06-01-2022 00:00"]) 
max(kit["07-01-2022 00:00"]) - min(kit["07-01-2022 00:00"]) 
max(kit["08-01-2022 00:00"]) - min(kit["08-01-2022 00:00"]) 
max(kit["09-01-2022 00:00"]) - min(kit["09-01-2022 00:00"]) 
max(kit["10-01-2022 00:00"]) - min(kit["10-01-2022 00:00"]) 
max(kit["11-01-2022 00:00"]) - min(kit["11-01-2022 00:00"]) 
max(kit["12-01-2022 00:00"]) - min(kit["12-01-2022 00:00"]) 
max(kit["01-01-2023 00:00"]) - min(kit["01-01-2023 00:00"]) 
max(kit["02-01-2023 00:00"]) - min(kit["02-01-2023 00:00"])
max(kit["03-01-2023 00:00"]) - min(kit["03-01-2023 00:00"]) 
max(kit["04-01-2023 00:00"]) - min(kit["04-01-2023 00:00"]) 
max(kit["05-01-2023 00:00"]) - min(kit["05-01-2023 00:00"]) 
max(kit["06-01-2023 00:00"]) - min(kit["06-01-2023 00:00"])
max(kit["07-01-2023 00:00"]) - min(kit["07-01-2023 00:00"]) 
max(kit["08-01-2023 00:00"]) - min(kit["08-01-2023 00:00"]) 
max(kit["09-01-2023 00:00"]) - min(kit["09-01-2023 00:00"]) 
max(kit["10-01-2023 00:00"]) - min(kit["10-01-2023 00:00"]) 
max(kit["11-01-2023 00:00"]) - min(kit["11-01-2023 00:00"]) 
max(kit["12-01-2023 00:00"]) - min(kit["12-01-2023 00:00"]) 


# Third moment business decision 
# skweness
kit['Total'].skew()
kit["04-01-2021 00:00"].skew()
kit["05-01-2021 00:00"].skew()
kit["06-01-2021 00:00"].skew()
kit["07-01-2021 00:00"].skew()
kit["08-01-2021 00:00"].skew()
kit["09-01-2021 00:00"].skew()
kit["10-01-2021 00:00"].skew()
kit["11-01-2021 00:00"].skew()
kit["12-01-2021 00:00"].skew()
kit["01-01-2022 00:00"].skew()
kit["02-01-2022 00:00"].skew()
kit["03-01-2022 00:00"].skew()
kit["04-01-2022 00:00"].skew()
kit["05-01-2022 00:00"].skew()
kit["06-01-2022 00:00"].skew()
kit["07-01-2022 00:00"].skew()
kit["08-01-2022 00:00"].skew()
kit["09-01-2022 00:00"].skew()
kit["10-01-2022 00:00"].skew()
kit["11-01-2022 00:00"].skew()
kit["12-01-2022 00:00"].skew()
kit["01-01-2023 00:00"].skew()
kit["02-01-2023 00:00"].skew()
kit["03-01-2023 00:00"].skew()
kit["04-01-2023 00:00"].skew()
kit["05-01-2023 00:00"].skew()
kit["06-01-2023 00:00"].skew()
kit["07-01-2023 00:00"].skew()
kit["08-01-2023 00:00"].skew()
kit["09-01-2023 00:00"].skew()
kit["10-01-2023 00:00"].skew()
kit["11-01-2023 00:00"].skew()
kit["12-01-2023 00:00"].skew()


# Fourth moment business decision
# kurtosis
kit['Total'].kurt()
kit["04-01-2021 00:00"].kurt()
kit["05-01-2021 00:00"].kurt()
kit["06-01-2021 00:00"].kurt()
kit["07-01-2021 00:00"].kurt()
kit["08-01-2021 00:00"].kurt()
kit["09-01-2021 00:00"].kurt()
kit["10-01-2021 00:00"].kurt()
kit["11-01-2021 00:00"].kurt()
kit["12-01-2021 00:00"].kurt()
kit["01-01-2022 00:00"].kurt()
kit["02-01-2022 00:00"].kurt()
kit["03-01-2022 00:00"].kurt()
kit["04-01-2022 00:00"].kurt()
kit["05-01-2022 00:00"].kurt()
kit["06-01-2022 00:00"].kurt()
kit["07-01-2022 00:00"].kurt()
kit["08-01-2022 00:00"].kurt()
kit["09-01-2022 00:00"].kurt()
kit["10-01-2022 00:00"].kurt()
kit["11-01-2022 00:00"].kurt()
kit["12-01-2022 00:00"].kurt()
kit["01-01-2023 00:00"].kurt()
kit["02-01-2023 00:00"].kurt()
kit["03-01-2023 00:00"].kurt()
kit["04-01-2023 00:00"].kurt()
kit["05-01-2023 00:00"].kurt()
kit["06-01-2023 00:00"].kurt()
kit["07-01-2023 00:00"].kurt()
kit["08-01-2023 00:00"].kurt()
kit["09-01-2023 00:00"].kurt()
kit["10-01-2023 00:00"].kurt()
kit["11-01-2023 00:00"].kurt()
kit["12-01-2023 00:00"].kurt()

# Different Visualizations on Data
# Histogram for Total column

import matplotlib.pyplot as plt

import seaborn as sns

plt.hist(kit['Total'],edgecolor='black')
plt.title('Histogram for Total')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.show()

sns.histplot(kit['Total'],kde=True,color='Red')
plt.title('Histogram for Total')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.show()

# checking whether the distribution is normal or not
from scipy import stats
import pylab

prob=stats.probplot(kit['Total'], dist= 'norm', plot=pylab)

# Plot for skewness and kurtosis
skewness_Total = kit['Total'].skew()
kurtosis_Total = kit['Total'].kurt()

# Create subplots for skewness and kurtosis
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot histogram for skewness
sns.histplot(kit['Total'], kde=True, color='blue', bins=30, ax=ax1)
ax1.set_title(f'Skewness: {skewness_Total:.2f}')

# Plot histogram for kurtosis
sns.histplot(kit['Total'], kde=True, color='orange', bins=30, ax=ax2)
ax2.set_title(f'Kurtosis: {kurtosis_Total:.2f}')

# Show the plot
plt.show()

# Boxenplot for Total column
sns.boxenplot(kit['Total'],orient='horizontal')
plt.title('Boxen plot for Total column')
plt.ylabel('Total')
plt.show()

# Boxplot for Total column
sns.boxplot(kit['Total'])
plt.title('Box plot for Total column')
plt.xlabel('Total')
plt.show()

# Barplot for Product type
product_type_counts = kit['Product type'].value_counts()
plt.figure(figsize=(10, 6))
product_type_counts.plot(kind='bar', color='skyblue')
plt.title('Bar Graph of Product Types', fontsize=16)
plt.xlabel('Product Type', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()

# Barplot for Customer Name
customer_name_counts = kit['Customer Name'].value_counts()
plt.figure(figsize=(10, 4))
customer_name_counts.plot(kind='bar', color='blue')
plt.title('Bar Graph of Customer Name', fontsize=16)
plt.xlabel('Customer Name', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()

# Bargraph showing Total sales per customer
customer_total = kit.groupby('Customer Name')['Total'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(customer_total['Customer Name'], customer_total['Total'], color='skyblue')
plt.title('Total Sales per Customer', fontsize=16)
plt.xlabel('Customer', fontsize=14)
plt.ylabel('Total', fontsize=14)
plt.xticks(rotation=90, ha='right')  
plt.show()

############################DATA PRE-PROCESSING#################################################
######TYPE CASTING #######
kit['Customer Code']=kit['Customer Code'].astype('str')

####### Handling Duplicates ######
kit_no_duplicate=kit.drop_duplicates(keep = 'last')
kit_no_duplicate
### It shows that there are no Duplicate values in the Dataset

####### Missing values ##########
kit_no_duplicate["04-01-2021 00:00"]=kit_no_duplicate["04-01-2021 00:00"].fillna(0)
kit_no_duplicate["05-01-2021 00:00"]=kit_no_duplicate["05-01-2021 00:00"].fillna(0)
kit_no_duplicate["06-01-2021 00:00"]=kit_no_duplicate["06-01-2021 00:00"].fillna(0)
kit_no_duplicate["07-01-2021 00:00"]=kit_no_duplicate["07-01-2021 00:00"].fillna(0)
kit_no_duplicate["08-01-2021 00:00"]=kit_no_duplicate["08-01-2021 00:00"].fillna(0)
kit_no_duplicate["09-01-2021 00:00"]=kit_no_duplicate["09-01-2021 00:00"].fillna(0)
kit_no_duplicate["10-01-2021 00:00"]=kit_no_duplicate["10-01-2021 00:00"].fillna(0)
kit_no_duplicate["11-01-2021 00:00"]=kit_no_duplicate["11-01-2021 00:00"].fillna(0)
kit_no_duplicate["12-01-2021 00:00"]=kit_no_duplicate["12-01-2021 00:00"].fillna(0)
kit_no_duplicate["01-01-2022 00:00"]=kit_no_duplicate["01-01-2022 00:00"].fillna(0)
kit_no_duplicate["02-01-2022 00:00"]=kit_no_duplicate["02-01-2022 00:00"].fillna(0)
kit_no_duplicate["03-01-2022 00:00"]=kit_no_duplicate["03-01-2022 00:00"].fillna(0)
kit_no_duplicate["04-01-2022 00:00"]=kit_no_duplicate["04-01-2022 00:00"].fillna(0)
kit_no_duplicate["05-01-2022 00:00"]=kit_no_duplicate["05-01-2022 00:00"].fillna(0)
kit_no_duplicate["06-01-2022 00:00"]=kit_no_duplicate["06-01-2022 00:00"].fillna(0)
kit_no_duplicate["07-01-2022 00:00"]=kit_no_duplicate["07-01-2022 00:00"].fillna(0)
kit_no_duplicate["08-01-2022 00:00"]=kit_no_duplicate["08-01-2022 00:00"].fillna(0)
kit_no_duplicate["09-01-2022 00:00"]=kit_no_duplicate["09-01-2022 00:00"].fillna(0)
kit_no_duplicate["10-01-2022 00:00"]=kit_no_duplicate["10-01-2022 00:00"].fillna(0)
kit_no_duplicate["11-01-2022 00:00"]=kit_no_duplicate["11-01-2022 00:00"].fillna(0)
kit_no_duplicate["12-01-2022 00:00"]=kit_no_duplicate["12-01-2022 00:00"].fillna(0)
kit_no_duplicate["01-01-2023 00:00"]=kit_no_duplicate["01-01-2023 00:00"].fillna(0)
kit_no_duplicate["02-01-2023 00:00"]=kit_no_duplicate["02-01-2023 00:00"].fillna(0)
kit_no_duplicate["03-01-2023 00:00"]=kit_no_duplicate["03-01-2023 00:00"].fillna(0)
kit_no_duplicate["04-01-2023 00:00"]=kit_no_duplicate["04-01-2023 00:00"].fillna(0)
kit_no_duplicate["05-01-2023 00:00"]=kit_no_duplicate["05-01-2023 00:00"].fillna(0)
kit_no_duplicate["06-01-2023 00:00"]=kit_no_duplicate["06-01-2023 00:00"].fillna(0)
kit_no_duplicate["07-01-2023 00:00"]=kit_no_duplicate["07-01-2023 00:00"].fillna(0)
kit_no_duplicate["08-01-2023 00:00"]=kit_no_duplicate["08-01-2023 00:00"].fillna(0)
kit_no_duplicate["09-01-2023 00:00"]=kit_no_duplicate["09-01-2023 00:00"].fillna(0)
kit_no_duplicate["10-01-2023 00:00"]=kit_no_duplicate["10-01-2023 00:00"].fillna(0)
kit_no_duplicate["11-01-2023 00:00"]=kit_no_duplicate["11-01-2023 00:00"].fillna(0)
kit_no_duplicate["12-01-2023 00:00"]=kit_no_duplicate["12-01-2023 00:00"].fillna(0)
kit_no_duplicate.isna().sum()
###### All the missing values are replaced with 0 ########


####### Outliers Treatment #########

Q1=kit_no_duplicate['Total'].quantile(0.25)
Q3=kit_no_duplicate['Total'].quantile(0.75)
IQR=Q3-Q1
upper_limit = Q3+(1.5*IQR)
lower_limit = Q1-(1.5*IQR)
outliers = kit_no_duplicate[(kit_no_duplicate['Total'] < lower_limit) | (kit_no_duplicate['Total'] > upper_limit)]
print(outliers)
## We can see that there are nearly 42 outliers present in our dataset

q1=kit_no_duplicate['04-01-2021 00:00'].quantile(0.25)
q3=kit_no_duplicate['04-01-2021 00:00'].quantile(0.75)
iqr=q3-q1
Upper_limit = q3+(1.5*iqr)
Lower_limit = q1-(1.5*iqr)
Outliers_04_01_2021 = kit_no_duplicate[(kit_no_duplicate['04-01-2021 00:00'] < Lower_limit) | (kit_no_duplicate['04-01-2021 00:00'] > Upper_limit)]
print(Outliers_04_01_2021)

q1=kit_no_duplicate['05-01-2021 00:00'].quantile(0.25)
q3=kit_no_duplicate['05-01-2021 00:00'].quantile(0.75)
iqr=q3-q1
Upper_limit = q3+(1.5*iqr)
Lower_limit = q1-(1.5*iqr)
Outliers_05_01_2021 = kit_no_duplicate[(kit_no_duplicate['05-01-2021 00:00'] < Lower_limit) | (kit_no_duplicate['05-01-2021 00:00'] > Upper_limit)]
print(Outliers_05_01_2021)

q1=kit_no_duplicate['06-01-2021 00:00'].quantile(0.25)
q3=kit_no_duplicate['06-01-2021 00:00'].quantile(0.75)
iqr=q3-q1
Upper_limit = q3+(1.5*iqr)
Lower_limit = q1-(1.5*iqr)
Outliers_06_01_2021 = kit_no_duplicate[(kit_no_duplicate['06-01-2021 00:00'] < Lower_limit) | (kit_no_duplicate['06-01-2021 00:00'] > Upper_limit)]
print(Outliers_06_01_2021)
######## We can see that the date columns also contains outliers

from feature_engine.outliers import Winsorizer
winsor_percentile=Winsorizer(capping_method='iqr', tail='both',fold=1.5)
df=winsor_percentile.fit_transform(kit_no_duplicate[['04-01-2021 00:00', '05-01-2021 00:00',
'06-01-2021 00:00', '07-01-2021 00:00', '08-01-2021 00:00',
'09-01-2021 00:00', '10-01-2021 00:00', '11-01-2021 00:00',
'12-01-2021 00:00', '01-01-2022 00:00', '02-01-2022 00:00',
'03-01-2022 00:00', '04-01-2022 00:00', '05-01-2022 00:00',
'06-01-2022 00:00', '07-01-2022 00:00', '08-01-2022 00:00',
'09-01-2022 00:00', '10-01-2022 00:00', '11-01-2022 00:00',
'12-01-2022 00:00', '01-01-2023 00:00', '02-01-2023 00:00',
'03-01-2023 00:00', '04-01-2023 00:00', '05-01-2023 00:00',
'06-01-2023 00:00', '07-01-2023 00:00', '08-01-2023 00:00',
'09-01-2023 00:00', '10-01-2023 00:00', '11-01-2023 00:00',
'12-01-2023 00:00','Total']])

Q1=df['Total'].quantile(0.25)
Q3=df['Total'].quantile(0.75)
IQR=Q3-Q1
upper_limit = Q3+(1.5*IQR)
lower_limit = Q1-(1.5*IQR)
outliers_total = df[(df['Total'] < lower_limit) | (df['Total'] > upper_limit)]
print(outliers_total)

Q1=df['04-01-2021 00:00'].quantile(0.25)
Q3=df['04-01-2021 00:00'].quantile(0.75)
IQR=Q3-Q1
upper_limit = Q3+(1.5*IQR)
lower_limit = Q1-(1.5*IQR)
outliers_w_04_01 = df[(df['04-01-2021 00:00'] < lower_limit) | (df['04-01-2021 00:00'] > upper_limit)]
print(outliers_w_04_01)

Q1=df['05-01-2021 00:00'].quantile(0.25)
Q3=df['05-01-2021 00:00'].quantile(0.75)
IQR=Q3-Q1
upper_limit = Q3+(1.5*IQR)
lower_limit = Q1-(1.5*IQR)
outliers_w_05_01 = df[(df['05-01-2021 00:00'] < lower_limit) | (df['05-01-2021 00:00'] > upper_limit)]
print(outliers_w_05_01)

Q1=df['06-01-2021 00:00'].quantile(0.25)
Q3=df['06-01-2021 00:00'].quantile(0.75)
IQR=Q3-Q1
upper_limit = Q3+(1.5*IQR)
lower_limit = Q1-(1.5*IQR)
outliers_w_06_01 = df[(df['06-01-2021 00:00'] < lower_limit) | (df['06-01-2021 00:00'] > upper_limit)]
print(outliers_w_06_01)
# We can see that all the outliers in the dataset has been treated

#Now let's create a new dataset combining the dataset with rest of categorical columns
kit_no_outliers=pd.concat([kit_no_duplicate[['Customer Code', 'Customer Name', 'KIT ITEM', 'OEM',
                                    'Item Description','Product type', 'Item Code']],df],axis=1)
######### The new dataframe does not contain any outliers #########

variance=kit_no_outliers[['04-01-2021 00:00', '05-01-2021 00:00',
'06-01-2021 00:00', '07-01-2021 00:00', '08-01-2021 00:00',
'09-01-2021 00:00', '10-01-2021 00:00', '11-01-2021 00:00',
'12-01-2021 00:00', '01-01-2022 00:00', '02-01-2022 00:00',
'03-01-2022 00:00', '04-01-2022 00:00', '05-01-2022 00:00',
'06-01-2022 00:00', '07-01-2022 00:00', '08-01-2022 00:00',
'09-01-2022 00:00', '10-01-2022 00:00', '11-01-2022 00:00',
'12-01-2022 00:00', '01-01-2023 00:00', '02-01-2023 00:00',
'03-01-2023 00:00', '04-01-2023 00:00', '05-01-2023 00:00',
'06-01-2023 00:00', '07-01-2023 00:00', '08-01-2023 00:00',
'09-01-2023 00:00', '10-01-2023 00:00', '11-01-2023 00:00',
'12-01-2023 00:00', 'Total']].var()
near_zero_variance=variance[variance<0.01]
print(near_zero_variance)
###### We can see that there are No Zero or near zero variance columns in the dataset #######

 ################# Normalization/Feature Scaling ###############
from sklearn.preprocessing import StandardScaler
s_scaler = StandardScaler()
kit_no_outliers['Total_Scaled'] = s_scaler.fit_transform(kit_no_outliers[['Total']])
kit_no_outliers['Total_Scaled']
#### Total Column has been scaled to the range between -3.14 to 3.14 ######
#### The data has been added as a new column to the dataset  ########

############## Data Transformation  ############
from feature_engine import transformation
yeo_transform=transformation.YeoJohnsonTransformer()
kit_no_outliers['Total_Transformed']=yeo_transform.fit_transform(kit_no_outliers[['Total']])
##### With the help of YeoJohnson Transformation the data is now normally i.e.symmetrically Distributed ########

##### Pushing the Cleaned Data into MYSQL #####
kit_no_outliers.to_sql('kit_clean_data', con = engine, if_exists = 'replace',
                       chunksize = None, index = False)
