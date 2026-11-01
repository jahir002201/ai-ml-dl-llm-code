import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Rahim", "Ayesha", "Karim"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE"],
    "Marks": [85, 92, 85, 78, 92],
})

print("Original data:")
print(df)

print("\nDuplicate rows:")
print(df[df.duplicated()])

# Keep the first occurrence of each complete duplicate row.
clean_df = df.drop_duplicates()
print("\nAfter removing complete duplicate rows:")
print(clean_df)

# Check duplicates based only on selected columns.
print("\nDuplicate names:")
print(df[df.duplicated(subset=["Name"], keep=False)])
