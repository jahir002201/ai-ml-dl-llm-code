import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Marks": [85, 92, 78],
})

print("Iterate over column names:")
for column in df.columns:
    print(column)

print("\nIterate over rows with iterrows:")
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Marks: {row['Marks']}")

print("\nRecommended row iteration with itertuples:")
for row in df.itertuples(index=False):
    print(f"{row.Name} scored {row.Marks}")
