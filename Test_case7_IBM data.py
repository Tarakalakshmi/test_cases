import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\User\\Downloads\\9.ibm.csv")
print(df.info())
#Q1)Find out the employee number and dept of employee who does overtime?
data=df[df['OverTime'] =='Yes']
overtime_employees=data[['EmployeeNumber', 'Department','OverTime']]
print(overtime_employees)

#Q2)Find out last 5 employees based on last promotion received?
promotions=df[df['YearsSinceLastPromotion'] > 0]
print(promotions.tail())

#Q3)Find out the list of employee whose income is more than the average income of all the employee’s present in the same department?
# Calculate average income for each department(using mean)
department_avg_income = df.groupby('Department')['MonthlyIncome'].mean()
def filter_high_income(row):
    department = row['Department']
    income = row['MonthlyIncome']
    return income > department_avg_income[department]
high_income_employees = df[df.apply(filter_high_income, axis=1)]
hie=high_income_employees[['EmployeeNumber', 'Department', 'MonthlyIncome']]
print(hie)


         #Going Deep into Data

#To find the employee who are the highest salary in monthly income.
employee=df['MonthlyIncome'].idxmax()
employee_data=df.loc[employee]
employee_with_highest_income=employee_data[['EmployeeNumber', 'MonthlyIncome']]
print(employee_with_highest_income)

#Train and Test the model using original dataset and report the performance on the test set including accuracy rate. 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
   # Load the original dataset (assuming df is your DataFrame)
   # For example, if 'Attrition' is the target variable:
X = df.drop(columns=['Attrition'])  # Features
y = df['Attrition']  # Target variable
   # Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X)
   # Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   # Initialize the Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
   # Train the model on the training data
clf.fit(X_train, y_train)
   # Predictions on the test set
predictions = clf.predict(X_test)
   # Calculate accuracy rate
accuracy = accuracy_score(y_test, predictions)
   # Report performance on the test set
print(f"Accuracy: {accuracy:.2f}")


#To find Employees, how many employees are worked as “Research Scientist” and “Sales Executive”.
employees=df['JobRole'].value_counts()
print(employees)

#To find the employee marital status as ascending to descending order by using dataset.
  #Ascending order
marital_status=df.sort_values(by='MaritalStatus',ascending=True)
print(marital_status[['EmployeeNumber', 'MaritalStatus']])
  #Descending order
ms=df.sort_values(by='MaritalStatus',ascending=False)
print(ms[['EmployeeNumber', 'MaritalStatus']])

#To find employees, who are in the medical field ?                  
medical_field=df[df['EducationField'] =='Medical']
print(medical_field[['EmployeeNumber', 'EducationField']])

#In employees how many of them are satisfaction with the environment.
empl=df[df['EnvironmentSatisfaction'] ==4].count()
print(empl[['EnvironmentSatisfaction']])

#Find out the list of employee whose income is more than the average income.
avg_income=df['MonthlyIncome'].mean()
high_income=df[df['MonthlyIncome'] > avg_income]
print(high_income[['EmployeeNumber', 'MonthlyIncome']])

#To find the AGEof employees more than 35 years.
Age_employees=df[df['Age'] >35]
print(Age_employees[['EmployeeNumber', 'Age']])

#In Business travel, how many number of employees are travel frequently.
traveler=df[df['BusinessTravel'] =='Travel_Frequently'].count()
print(traveler[['BusinessTravel']])

#Find out the list of employees, how many years spent with current manager
manager=df[df['YearsWithCurrManager'] >0]
print(manager[['EmployeeNumber', 'YearsWithCurrManager']])

#To find the employee ,how many of them leaving the company.
leaving_employees=df[df['Attrition'] =='Yes'].count()
print(leaving_employees[['Attrition']])

#Show one scatter plot,it is your choice to show which two features you want to use, by using original dataset.
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.scatter(df['Age'], df['MonthlyIncome'],color='red',alpha=0.5)
plt.title("Age vs Monthly income")
plt.xlabel("Age")
plt.ylabel("MonthlyIncome")
plt.grid(True)
plt.show()

#Plot two subplots in one figure by using the dataset.
import matplotlib.pyplot as plt
   # Assuming df is your DataFrame
   # Create a figure with two subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
   # First Subplot: Histogram of Age
axs[0].hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Age Distribution')
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Count')
   # Second Subplot: Bar chart of Attrition
attrition_counts = df['Attrition'].value_counts()
axs[1].bar(attrition_counts.index, attrition_counts.values, color='green', alpha=0.7)
axs[1].set_title('Attrition')
axs[1].set_xlabel('Attrition')
axs[1].set_ylabel('Count')
   # Adjust layout and display the plot
plt.tight_layout()
plt.show()


#Choose an attribute and generate a boxplot by using dataset.
import matplotlib.pyplot as plt
   # Assuming df is your DataFrame
   # Create a boxplot for MonthlyIncome
plt.figure(figsize=(8, 6))
plt.boxplot(df['MonthlyIncome'], vert=False, widths=0.7, patch_artist=True)
plt.title('Monthly Income Boxplot')
plt.xlabel('Monthly Income')
plt.show()






