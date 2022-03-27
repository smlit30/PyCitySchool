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

#print(district_summary_df)

def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100.0

# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

#print(district_summary_df["Total Students"])

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

#print(district_summary_df["Total Budget"])
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

#print(district_summary_df)

# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
#print(district_summary_df)

per_school_types = school_data_df.set_index(["school_name"])["type"]
#print(per_school_types)
df = pd.DataFrame(per_school_types)
#print(df)
# Calculate the total student count.
per_school_counts = school_data_df["size"]
#print(per_school_counts)
# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
#print(per_school_counts)
per_school_counts = school_data_complete_df["school_name"].value_counts()
#print(per_school_counts)
# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
#print(per_school_budget)
# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
#print(per_school_capita)
# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]
#print(student_school_math)
# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
#print(per_school_averages)
# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
 # To get the passing percentages, we need to:
 # 1. Determine what is the passing grade.
 # 2. Get the number of students who passed math and reading.
 # 3. Get the students who passed math and passed reading
 
 # Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

#print(per_school_passing_reading)
# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
# Calculate the students who passed both math and reading.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

#print(per_passing_math_reading.head())
# Calculate the number of students who passed both math and reading.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
# Calculate the overall passing percentage.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100
#print(per_overall_passing_percentage)

per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})


per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Reorder the columns in the order you want them to appear.
new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
per_school_summary_df = per_school_summary_df[new_column_order]

# Display the data frame
print(per_school_summary_df)