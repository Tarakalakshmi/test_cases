#FDNY dataset

#1.view and import data
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\User\\Downloads\\14.FDNY.csv")
#analyze the data
print(df)
data=df.drop_duplicates()
print(data)
data.info()
data=df.describe()
print(data)
column_names=df.columns
print(column_names)
print(df.index)
#3.Find the total number of records for each attribute
print(df.count())
print(df.info(type))
#4.Find the total number of fire department facilities in each borough
borough=df['Borough'].count()
print(borough)
#5.Find the total number of facilities in Manhattan
count=df['Borough'].value_counts()['Manhattan']
print(count)







