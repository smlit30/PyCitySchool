import pandas as pd 
import os  

school_data_to_load = "modules/Module 4 - Python & Pandas/Resources/schools_complete.csv"
student_data_to_load = "modules/Module 4 - Python & Pandas/Resources/students_complete.csv"
mgrades_path = "modules/Module 4 - Python & Pandas/Resources/missing_grades.csv"

school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)
missing_grade_df = pd.read_csv(mgrades_path)
missing_grade_df.fillna(85)


print(student_data_df.count())
print(student_data_df.isnull().sum())
print(missing_grade_df)

student_names = student_data_df["student_name"].tolist()

#for name in student_names:
   # print(name.split(), len(name.split()))
   
students_to_fix = []
 
for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)
        
print(len(students_to_fix)) 

prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])
        
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])
        
#print(set(suffixes))
#print(set(prefixes))

prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")    
    
#print(student_data_df.head())

student_names = student_data_df["student_name"].tolist()

# Create a new list and use it for the for loop to iterate through the list.
students_fixed = []

# Use an if statement to check the length of the name.

# If the name is greater than or equal to 3, add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_fixed.append(name)
        
print(len(students_fixed))