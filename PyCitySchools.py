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
        
#print(len(students_fixed))

school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
#print(school_data_complete_df.head())

student_count = school_data_complete_df["Student ID"].count()
print(student_count)

#print(school_data_complete_df["Student ID"].count())
school_count = school_data_df["school_name"].count()
school_count_2 = school_data_complete_df["school_name"].unique()
#print(school_count_2)

total_budget = school_data_df["budget"].sum()
print(total_budget)

average_reading_score = school_data_complete_df["reading_score"].mean()
print(average_reading_score)

average_math_score = school_data_complete_df["math_score"].mean()
print(average_math_score)

passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70

passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]

passing_math_count = passing_math["student_name"].count()
passing_reading_count = passing_reading["student_name"].count()

print(passing_math_count)
print(passing_reading_count)

passing_math_percentage = passing_math_count / student_count * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / student_count * 100

print(passing_math_percentage)
print(passing_reading_percentage)

passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

#print(passing_math_reading.head())

overall_passing_math_reading_count = passing_math_reading["student_name"].count()
#print(overall_passing_math_reading_count)
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
#print(overall_passing_percentage)


print("See below for district summary statistics")

district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])

print(district_summary_df)

def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100.0

# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

#print(district_summary_df["Total Students"])

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

print(district_summary_df["Total Budget"])
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

print(district_summary_df)

# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
print(district_summary_df)