# Optimizing Kit Item Distribution Project

![Kit Item Optimization](https://thumbs.dreamstime.com/b/auto-spare-parts-car-white-background-set-many-isolated-items-shop-aftermarket-auto-spare-parts-car-166776282.jpg)

## Project Overview

This project focuses on optimizing the kit item distribution to maximize supply consistency and find a way to source the vendors with unique kit items, reduce costs, and enhance overall efficiency. By leveraging data analytics and visualization tools, this project aims to provide actionable insights for better decision-making.

## Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Business Objective](#business-objective)
- [Business Constraint](#business-constraint)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Usage](#usage)
- [Dashboard](#interactive-dashboards)
- [Project Structure](#project-structure)


## Business Problem

A Leading automotive manufacturer, facing difficulty in efficiently sourcing and providing unique kit items from various vendors to meet customer demands.

## Business Objective

Maximize efficient kit delivery

## Business Constraint

Maximize the supply consistency

## Tech Stack

- **Python**
- **MySQL**
- **Matplotlib**
- **Seaborn**
- **Power BI**
- **Looker Studio**
- **Excel**

## Features

- **Data Cleaning and Preprocessing**: Identification and removal of outliers, handling of missing values, and ensuring data consistency.
- **Data Exploration and Analysis**: In-depth analysis using Matplotlib and Seaborn to uncover patterns and insights.
- **Interactive Dashboards**: Dynamic dashboards created with Power BI, Looker Studio, and Excel for effective data visualization and reporting.

  

## Usage

1. Load the dataset:
    ```python
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
    ```
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-06%20135144.png"/>
From the Above image we can see that there are 307 records and 41 features in the dataset.

2. Run the data cleaning and preprocessing scripts:
    ```python
              ######TYPE CASTING #######
        kit['Customer Code']=kit['Customer Code'].astype('str')
        Changed the data type from Numeric to String
    
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

    ```

3. Perform data exploration and visualization:
    ```python
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

    ```

<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-06%20140008.png" width="300" height="300"/>  
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20143935.png" width="300" height="300"/>
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20143401.png" width="300" height="300"/>
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20143436.png" width="300" height="300"/>
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20143424.png" width="300" height="300"/> 
The above chart shows the probplot before transformation.

<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20143645.png" width="300" height="300"/>
This chart is showing the distribution after transforming the values of features.

## Interactive dashboards:
    Open the Power BI / Looker Studio / Excel files in the `dashboards` directory to view the interactive visualizations.
<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20144324.png"/>

<img src="https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/New%20folder/Screenshot%202024-07-05%20144413.png"/>

## Project Structure
kit-item-optimization/
- data/
  - raw_data.csv
- scripts/
  - data_cleaning.py
  - data_analysis.py
- dashboards/
  - dashboard.pbix
  - dashboard.looker
  - dashboard.xlsx
- images/
  - [charts.png](https://github.com/NaveenM-10/optimization-kit-item-distribution/tree/main/New%20folder)
  - [README.md](https://github.com/NaveenM-10/optimization-kit-item-distribution/blob/main/README.md)
