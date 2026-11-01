import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Marks": [85, 92, 78],
    "Age": [21, 23, 20],
})

# Add a new column.
df["Passed"] = df["Marks"] >= 40

# Update a value using loc.
df.loc[df["Name"] == "Ayesha", "Marks"] = 88

# Rename a column.
df = df.rename(columns={"Marks": "Score"})

# Drop a column and keep the returned DataFrame.
df = df.drop(columns=["Age"])

print("Modified DataFrame:")
print(df)
