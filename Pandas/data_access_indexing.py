import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Age": [21, 23, 20],
    "Marks": [85, 92, 78],
}, index=["S01", "S02", "S03"])

print("Full DataFrame:")
print(df)

print("\nSelect one column:")
print(df["Name"])

print("\nSelect multiple columns:")
print(df[["Name", "Marks"]])

print("\nSelect a row by its index label:")
print(df.loc["S02"])
