import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", None, "Nila", "Ayesha"],
    "Age": [21, np.nan, 20, 22, np.nan],
    "Marks": [85, 92, np.nan, 90, 78],
})

print("Original data:")
print(df)

print("\nMissing-value count per column:")
print(df.isna().sum())

# Fill missing text with a label.
df["Name"] = df["Name"].fillna("Unknown")

# Fill numeric missing values with each column's mean.
for column in ["Age", "Marks"]:
    df[column] = df[column].fillna(df[column].mean())

print("\nAfter filling missing values:")
print(df)

# To remove rows containing missing values instead, use:
# cleaned = df.dropna()
