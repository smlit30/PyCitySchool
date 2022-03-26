import pandas as pd 
import os  

school_data_to_load = "modules/Module 4 - Python & Pandas/Resources/schools_complete.csv"
student_data_to_load = "modules/Module 4 - Python & Pandas/Resources/students_complete.csv"

school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)


print(student_data_df.head())