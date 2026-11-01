import pandas as pd

original = pd.DataFrame({
    "Name": ["Rahim", "Karim", "Ayesha"],
    "Marks": [85, 92, 78],
})

# A deep copy can be changed without changing the original DataFrame.
copied = original.copy(deep=True)
copied.loc[0, "Marks"] = 100

print("Original DataFrame:")
print(original)
print("\nCopied DataFrame after modification:")
print(copied)
