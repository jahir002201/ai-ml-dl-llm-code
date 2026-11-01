import pandas as pd

df = pd.DataFrame({
    "Department": ["CSE", "CSE", "EEE", "EEE", "BBA", "BBA"],
    "Name": ["Rahim", "Ayesha", "Karim", "Nila", "Sakib", "Mitu"],
    "Marks": [85, 78, 92, 88, 90, 82],
})

# Group rows by department and calculate summary statistics.
summary = df.groupby("Department")["Marks"].agg(
    Student_Count="count",
    Average_Marks="mean",
    Highest_Marks="max",
    Lowest_Marks="min",
)

print("Department-wise analysis:")
print(summary)

print("\nStudents in each department:")
for department, group in df.groupby("Department"):
    print(f"\n{department}:")
    print(group[["Name", "Marks"]].to_string(index=False))
