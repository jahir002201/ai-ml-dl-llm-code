import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha", "Nila"],
    "Department": ["CSE", "EEE", "CSE", "BBA"],
    "Marks": [85, 92, 78, 90],
}, index=["S01", "S02", "S03", "S04"])

# loc selects using row/column labels.
print("One row:")
print(df.loc["S02"])

print("\nSelected rows and columns:")
print(df.loc[["S01", "S03"], ["Name", "Marks"]])

print("\nRows where Department is CSE:")
print(df.loc[df["Department"] == "CSE", ["Name", "Marks"]])
