import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha", "Nila"],
    "Age": [21, 23, 20, 22],
    "Marks": [85, 92, 78, 90],
})

# iloc selects using integer positions (Python-style, end-exclusive slices).
print("First row:")
print(df.iloc[0])

print("\nRows 1 and 2:")
print(df.iloc[1:3])

print("\nFirst three rows, Name and Marks columns:")
print(df.iloc[0:3, [0, 2]])

print("\nLast row:")
print(df.iloc[-1])
