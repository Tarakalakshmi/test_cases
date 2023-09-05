#About Aadhar dataset
import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\User\\Downloads\\11.abc.csv")
print(df.info())

#1.Find out the total number of cards approved by States.
state_approved = df.groupby('State')['Aadhaar generated'].sum().reset_index()
print("Tota number of cards approved by states:",state_approved)

#2.Find out the total number of cards Enrolment rejected by states.
state_rejected = df.groupby('State')['Enrolment Rejected'].sum().reset_index()
print("Total number of cards rejected by states:",state_rejected)

#3.Find out the total number of cards approved by Districts.
district_approved = df.groupby('District')['Aadhaar generated'].sum().reset_index()
print("The number of aadhaar cards approved by Districts:",district_approved)

#4.Find out the total number of cards rejected by Districts.
district_rejected = df.groupby('District')['Enrolment Rejected'].sum().reset_index()
print("Total number of cards rejected by states:",district_rejected)

#5.Total Count Gender Based
data=df['Gender'].value_counts()
print(data)

#6.Count Records age <25, age between 25 &35, age>45
age_lt_25 = len(df[df['Age'] < 25])
age_between_25_35 = len(df[(df['Age'] >= 25) & (df['Age'] <= 35)])
age_gt_45 = len(df[df['Age'] > 45])
print("Number of records with age < 25:", age_lt_25)
print("Number of records with age between 25 and 35:", age_between_25_35)
print("Number of records with age > 45:", age_gt_45)
