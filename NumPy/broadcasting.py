import numpy as np

# Example 1: Scalar Broadcasting
a = np.array([10, 20, 30])
print("Scalar Addition:", a + 5)

# Example 2: Scalar Multiplication
print("Scalar Multiplication:", a * 2)

# Example 3: Same Shape
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("Same Shape:", a + b)

# Example 4: Different Shape
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])
print("Different Shape:\n", a + b)

# Example 5: Column Broadcasting
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [10],
    [20]
])

print("Column Broadcasting:\n", a + b)

# Example 6: Multiplication Broadcasting
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([2, 3, 4])
print("Multiplication:\n", a * b)

# Example 7: Division Broadcasting
prices = np.array([100, 200, 300])
discount = 10

print("Discount:", prices * discount / 100)

# Example 8: Broadcasting with reshape
a = np.array([1, 2, 3])
b = np.array([10, 20])

result = a[:, np.newaxis] + b
print("Newaxis Broadcasting:\n", result)

# Example 9: Broadcasting Shape
a = np.ones((3, 1))
b = np.ones((1, 4))

result = a + b
print("Result Shape:", result.shape)
print(result)

# Example 10: Normalize Rows
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

row_sum = data.sum(axis=1, keepdims=True)
normalized = data / row_sum

print("Normalized:\n", normalized)

# Example 11: Add Row and Column
row = np.array([1, 2, 3])
column = np.array([[10], [20], [30]])

print("Result:\n", row + column)

# Example 12: Broadcasting with comparison
marks = np.array([
    [70, 80, 90],
    [60, 50, 40]
])

passing_marks = np.array([40, 50, 60])

print("Passed:\n", marks >= passing_marks)