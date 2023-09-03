#The Salary_dataset(Q/A)
#Salary dataset
#answer for 1 and 2 questions
import pandas as pd
df=pd.read_csv("C:\\Users\\User\\Downloads\\Sf_Salaries (1).csv")
print(df)
df.info()

#3.What is the average on BasePay ?
column_name='BasePay'
average=df[column_name].mean()
print("Average of BasePay:",average)

#4.What is the highest amount of OvertimePay in dataset ?
max_OTP=df['OvertimePay'].max()
print("maximum of Over time pay:",max_OTP)

#5.What is the Job Title of JOSEPH DRISCOLL?
joseph_row=df[df['EmployeeName']== 'JOSEPH DRISCOLL']
joseph_job_title=joseph_row['JobTitle'].values[0]
print("Joseph job title:",joseph_job_title)

#6.How much does JOSEPH DRISCOLL make(Including Benefits)?
joseph_income=df[df['EmployeeName']== 'JOSEPH DRISCOLL']
joseph_totalincome=joseph_income['TotalPayBenefits'].values[0]
print("Joseph TotalPay benefits:",joseph_totalincome)

#7.What is the name of highest paid person(Including benefits)?
highest_paid=df[df['TotalPayBenefits']==df['TotalPayBenefits'].max()]
highest_paid_person=highest_paid['EmployeeName'].values[0]
print("Highest paid person:",highest_paid_person)

#8.What is the name of lowest paid person(Including benefits)?
lowest_paid=df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]
lowest_paid_person=lowest_paid['EmployeeName'].values[0]
print("lowest paid person:",lowest_paid_person)

#9.What was the average(mean) BasePay of all employees per year ? (2011 - 2014) ?
avg_bp_year=df.groupby('Year')['BasePay'].mean()
print("Average basepay per year:",avg_bp_year)

#10.How many Unique Job Titles are there ?
unique_job_titles_count = df['JobTitle'].nunique()
print("The number of unique job titles is:", unique_job_titles_count)

#11.What are the top 5 most common jobs ?
top_5_common_jobs=df['JobTitle'].value_counts().head(5)
print("Top 5 most common jobs:",top_5_common_jobs)











