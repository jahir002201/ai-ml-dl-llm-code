import numpy as np

# Example 1: Import NumPy
print("NumPy Version:", np.__version__)

# Example 2: Create Array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Example 3: Array Addition
print("Addition:", arr + 5)

# Example 4: Array Subtraction
print("Subtraction:", arr - 5)

# Example 5: Array Multiplication
print("Multiplication:", arr * 2)

# Example 6: Array Division
print("Division:", arr / 2)

# Example 7: Array Power
print("Power:", arr ** 2)

# Example 8: Comparison
print("Greater than 25:", arr > 25)

# Example 9: Sum
print("Sum:", np.sum(arr))

# Example 10: Maximum and Minimum
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Example 11: Python List vs NumPy Array
my_list = [1, 2, 3]
my_array = np.array([1, 2, 3])

print("List * 2:", my_list * 2)
print("Array * 2:", my_array * 2)