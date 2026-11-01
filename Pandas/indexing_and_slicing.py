import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha", "Nila", "Sakib"],
    "Marks": [85, 92, 78, 90, 66],
    "Age": [21, 23, 20, 22, 24],
})

print("First three rows:")
print(df[:3])

print("\nEvery second row:")
print(df[::2])

print("\nRows 1 through 3, using iloc (end-exclusive):")
print(df.iloc[1:4])

print("\nMarks column, first three rows:")
print(df.loc[:2, "Marks"])
