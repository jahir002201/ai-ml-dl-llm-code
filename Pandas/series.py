import pandas as pd

# A Series is a one-dimensional labeled array.
marks = pd.Series([85, 92, 78, 90], index=["Rahim", "Karim", "Ayesha", "Nila"], name="Marks")

print("Complete Series:")
print(marks)

print("\nValue for Karim:", marks["Karim"])
print("\nMarks greater than 80:")
print(marks[marks > 80])
print("\nBasic statistics:")
print(marks.describe())
