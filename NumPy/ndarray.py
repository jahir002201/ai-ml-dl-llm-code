import numpy as np

# Example 1: 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Example 2: 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D Array:\n", arr2)

# Example 3: 3D Array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D Array:\n", arr3)

# Example 4: Array Type
print("Type:", type(arr1))

# Example 5: Indexing
print("First Element:", arr1[0])
print("Last Element:", arr1[-1])

# Example 6: Slicing
print("Slice:", arr1[1:4])

# Example 7: Negative Indexing
print("Negative Index:", arr1[-2])

# Example 8: 2D Indexing
print("2D Element:", arr2[1, 2])

# Example 9: 2D Row
print("First Row:", arr2[0])

# Example 10: 2D Column
print("Second Column:", arr2[:, 1])

# Example 11: Boolean Indexing
print("Greater than 3:", arr1[arr1 > 3])

# Example 12: Reverse Array
print("Reverse:", arr1[::-1])