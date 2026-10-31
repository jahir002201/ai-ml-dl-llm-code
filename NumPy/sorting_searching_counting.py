import numpy as np

# Example 1: sort()
arr1 = np.array([50, 10, 40, 20, 30])
print("Sort:", np.sort(arr1))

# Example 2: Descending Sort
print("Descending:", np.sort(arr1)[::-1])

# Example 3: 2D Sort
arr2 = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

print("Row Sort:\n", np.sort(arr2, axis=1))
print("Column Sort:\n", np.sort(arr2, axis=0))

# Example 4: argsort()
arr3 = np.array([40, 10, 30, 20])
print("Argsort:", np.argsort(arr3))

# Example 5: argmax()
print("Maximum Index:", np.argmax(arr3))

# Example 6: argmin()
print("Minimum Index:", np.argmin(arr3))

# Example 7: where()
arr4 = np.array([10, 20, 30, 40, 50])
print("Where:", np.where(arr4 > 25))

# Example 8: searchsorted()
arr5 = np.array([10, 20, 30, 40, 50])
print("Searchsorted:", np.searchsorted(arr5, 35))

# Example 9: count_nonzero()
arr6 = np.array([0, 1, 0, 2, 3, 0, 4])
print("Nonzero Count:", np.count_nonzero(arr6))

# Example 10: unique()
arr7 = np.array([1, 2, 2, 3, 3, 3, 4])
print("Unique:", np.unique(arr7))

# Example 11: Unique with Counts
values, counts = np.unique(arr7, return_counts=True)
print("Values:", values)
print("Counts:", counts)

# Example 12: Boolean Search
arr8 = np.array([10, 20, 30, 40, 50])
print("Greater than 25:", arr8[arr8 > 25])

# Example 13: Multiple Conditions
arr9 = np.array([10, 20, 30, 40, 50, 60])
result = arr9[(arr9 >= 20) & (arr9 <= 50)]
print("Between 20 and 50:", result)

# Example 14: isin()
arr10 = np.array([10, 20, 30, 40, 50])
print("Isin:", np.isin(arr10, [20, 40]))

# Example 15: lexsort()
names = np.array(["Karim", "Rahim", "Jamal"])
marks = np.array([80, 90, 80])

indices = np.lexsort((names, marks))

print("Sorted Names:", names[indices])
print("Sorted Marks:", marks[indices])

# Example 16: extract()
arr11 = np.array([10, 15, 20, 25, 30])
print("Extract:", np.extract(arr11 > 20, arr11))

# Example 17: flatnonzero()
arr12 = np.array([0, 10, 0, 20, 30])
print("Nonzero Index:", np.flatnonzero(arr12))