import pandas as pd

# A DataFrame is a two-dimensional table with rows and columns.
data = {
    "Name": ["Rahim", "Karim", "Ayesha", "Nila"],
    "Age": [21, 23, 20, 22],
    "Department": ["CSE", "EEE", "CSE", "BBA"],
    "Marks": [85, 92, 78, 90],
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nFirst two rows:")
print(df.head(2))
