import pandas as pd

df = pd.DataFrame({
    "Department": ["CSE", "CSE", "EEE", "EEE", "BBA"],
    "Marks": [85, 78, 92, 88, 90],
    "Age": [21, 20, 23, 22, 24],
})

print("Total marks:", df["Marks"].sum())
print("Average marks:", df["Marks"].mean())
print("Maximum marks:", df["Marks"].max())
print("Minimum marks:", df["Marks"].min())

print("\nMultiple aggregations:")
print(df[["Marks", "Age"]].agg(["count", "mean", "min", "max"]))
