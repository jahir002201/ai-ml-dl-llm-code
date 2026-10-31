import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# Example 1: ndim
print("Dimensions:", arr.ndim)

# Example 2: shape
print("Shape:", arr.shape)

# Example 3: size
print("Size:", arr.size)

# Example 4: dtype
print("Data Type:", arr.dtype)

# Example 5: itemsize
print("Item Size:", arr.itemsize)

# Example 6: nbytes
print("Total Bytes:", arr.nbytes)

# Example 7: Integer Data Type
a = np.array([1, 2, 3], dtype=np.int32)
print("Integer:", a.dtype)

# Example 8: Float Data Type
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)
print("Float:", b.dtype)

# Example 9: Boolean Data Type
c = np.array([True, False, True])
print("Boolean:", c.dtype)

# Example 10: String Data Type
d = np.array(["Apple", "Banana", "Mango"])
print("String:", d.dtype)

# Example 11: Type Conversion
numbers = np.array([1.5, 2.7, 3.9])
converted = numbers.astype(int)

print("Original:", numbers)
print("Converted:", converted)

# Example 12: Complex Data Type
e = np.array([1+2j, 3+4j])
print("Complex:", e.dtype)