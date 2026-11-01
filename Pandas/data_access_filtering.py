import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha", "Nila", "Sakib"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "CSE"],
    "Marks": [85, 92, 78, 90, 66],
    "Age": [21, 23, 20, 22, 24],
})

# Filter with one condition.
print("Marks above 80:")
print(df[df["Marks"] > 80])

# Combine conditions with & (and) and | (or).
print("\nCSE students with marks >= 80:")
print(df[(df["Department"] == "CSE") & (df["Marks"] >= 80)])

print("\nStudents in CSE or EEE:")
print(df[df["Department"].isin(["CSE", "EEE"])])
