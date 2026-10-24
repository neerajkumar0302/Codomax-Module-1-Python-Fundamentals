# Codomax Module 1 - Python Fundamentals
# Intern ID: CDS/INT/202695385 | Neeraj Kumar

print("=== Python & Data Science Fundamentals ===")

# 1. Python Basics
name = "Neeraj Kumar"
skills = ["Python", "SQL", "Pandas", "Numpy"]
print(f"Name: {name}, Skills: {skills}")

# 2. Data Analysis with Pandas & Numpy
import pandas as pd
import numpy as np

data = {
    "Name": ["Neeraj", "Aman", "Priya", "Rahul", "Sneha"],
    "Python": [85, 90, 78, 92, 88],
    "SQL": [80, 85, 82, 90, 75]
}
df = pd.DataFrame(data)
print("\nStudent Data:\n", df)
print("\nAverage Python Score:", df["Python"].mean())
print("Top Scorer:", df.sort_values(by="Python", ascending=False).iloc[0]["Name"])
