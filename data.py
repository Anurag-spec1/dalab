# //create a dataset of your class 
# a.find the best student on the basis of marks
# b.find maximum marks in data analytics and print the name of student 
# c.replace the null value with mean
# d.find the average of your class in da
# e.print first five rows of your dataset
# f.print last ew column of the data structure


import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Arjun", "Pooja", "Rohit"],
    "Maths": [85, 90, 78, 92, 88, 76, 95],
    "Data_Analytics": [80, 85, None, 90, 87, None, 93],
    "English": [75, 88, 70, 85, 82, 78, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


df["Total"] = df[["Maths", "Data_Analytics", "English"]].sum(axis=1)

best_student = df.loc[df["Total"].idxmax()]
print("\nBest Student:")
print(best_student["Name"])

max_da_student = df.loc[df["Data_Analytics"].idxmax()]
print("\nStudent with Maximum Data Analytics Marks:")
print(max_da_student["Name"])