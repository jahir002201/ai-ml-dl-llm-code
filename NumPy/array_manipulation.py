import numpy as np

# Example 1: append()
arr1 = np.array([1, 2, 3])
print("Append:", np.append(arr1, 4))

# Example 2: insert()
arr2 = np.array([10, 20, 30])
print("Insert:", np.insert(arr2, 1, 15))

# Example 3: delete()
arr3 = np.array([10, 20, 30, 40])
print("Delete:", np.delete(arr3, 1))

# Example 4: concatenate()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Concatenate:", np.concatenate((a, b)))

# Example 5: stack()
print("Stack:\n", np.stack((a, b)))

# Example 6: vstack()
print("Vstack:\n", np.vstack((a, b)))

# Example 7: hstack()
print("Hstack:", np.hstack((a, b)))

# Example 8: dstack()
print("Dstack:\n", np.dstack((a, b)))

# Example 9: split()
arr4 = np.array([10, 20, 30, 40, 50, 60])
print("Split:", np.split(arr4, 3))

# Example 10: array_split()
arr5 = np.array([1, 2, 3, 4, 5])
print("Array Split:", np.array_split(arr5, 3))

# Example 11: where()
arr6 = np.array([10, 20, 30, 40])
print("Where:", np.where(arr6 > 20))

# Example 12: clip()
arr7 = np.array([5, 15, 25, 35, 45])
print("Clip:", np.clip(arr7, 10, 30))

# Example 13: unique()
arr8 = np.array([1, 2, 2, 3, 3, 4])
print("Unique:", np.unique(arr8))

# Example 14: flip()
arr9 = np.array([1, 2, 3, 4, 5])
print("Flip:", np.flip(arr9))

# Example 15: delete duplicates
arr10 = np.array([10, 20, 10, 30, 20])
print("Unique Values:", np.unique(arr10))

# Example 16: copy()
original = np.array([1, 2, 3])
copied = original.copy()
copied[0] = 100

print("Original:", original)
print("Copied:", copied)

# Example 17: Sorting in place
arr11 = np.array([5, 2, 4, 1, 3])
arr11.sort()
print("Sorted:", arr11)