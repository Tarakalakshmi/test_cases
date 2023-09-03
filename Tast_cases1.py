#Student: This dataset contains name and roll number of students in a class 
#Results: This dataset contains roll number and result (Fail or Pass) of students 


import numpy as np
import pandas as pd
df2=pd.DataFrame({"names":['vineet','hisham','raj','ajeet','sujit','ramesh','priya','priyanka','suresh','ritesh',
                           'hitesh','jatin','chitesh','suman','raman','aman','ravi','shravi','chavvi','himanshu'],
                  "rno":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']})
df3=pd.DataFrame({"results":['fail','fail','pass','pass','fail','pass','fail','pass','pass','pass',
                             'pass','fail','fail','fail','pass','fail','pass','fail','pass','pass'],
                  "rno":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']})
print(df2)
print(df3)

#prblm1:
#Analyse the given datasets
and print the student names who have successfully cleared the exam.
data=pd.merge(df2,df3,how="inner",on="rno")
passed_students=data[data['results']=='pass']
print(passed_students['names'])

#prblm2:
#Count Number Of Students(Pass/Fail)
print(passed_students.count())
result_counts = data['results'].value_counts()
print(result_counts)
#value_count will help to count the particular items that are only specified.

#prblm3
#Arrange Student Names Alpha Based
sorted_data=data.sort_values(by="names")
print(sorted_data)
