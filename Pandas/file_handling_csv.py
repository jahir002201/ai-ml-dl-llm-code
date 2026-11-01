import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Age": [21, 23, 20],
    "Marks": [85, 92, 78],
})

# Write a CSV file, then read it back.
df.to_csv("students.csv", index=False)
loaded_df = pd.read_csv("students.csv")

print("CSV data loaded successfully:")
print(loaded_df)
