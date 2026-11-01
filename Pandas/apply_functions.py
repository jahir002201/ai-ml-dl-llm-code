import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Marks": [85, 92, 38],
})

# Apply a function to every value in a Series.
df["Grade"] = df["Marks"].apply(
    lambda mark: "A" if mark >= 80 else ("B" if mark >= 50 else "F")
)

# Apply a function to each row.
df["Result"] = df.apply(
    lambda row: "Pass" if row["Marks"] >= 40 else "Fail",
    axis=1,
)

print(df)

# For simple arithmetic or comparisons, prefer vectorized operations
# such as df["Marks"] * 2 instead of apply() where possible.
