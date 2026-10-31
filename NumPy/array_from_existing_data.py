import numpy as np

# Example 1: Create from List
my_list = [10, 20, 30, 40]
arr1 = np.array(my_list)
print("From List:", arr1)

# Example 2: Create from Tuple
my_tuple = (10, 20, 30, 40)
arr2 = np.array(my_tuple)
print("From Tuple:", arr2)

# Example 3: Create from Nested List
data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print("Nested List:\n", arr3)

# Example 4: Using asarray()
arr4 = np.asarray(my_list)
print("Asarray:", arr4)

# Example 5: Using copy()
original = np.array([1, 2, 3])
copied = original.copy()

copied[0] = 100

print("Original:", original)
print("Copied:", copied)

# Example 6: Using frombuffer()
data = b'\x01\x02\x03\x04'
arr5 = np.frombuffer(data, dtype=np.uint8)
print("From Buffer:", arr5)

# Example 7: Using fromiter()
numbers = (x for x in range(1, 6))
arr6 = np.fromiter(numbers, dtype=int)
print("From Iterator:", arr6)

# Example 8: Create from String List
names = np.array(["Rahim", "Karim", "Jamal"])
print("Names:", names)

# Example 9: Create with Data Type
prices = np.array([100, 200, 300], dtype=float)
print("Prices:", prices)

# Example 10: Memory Sharing
a = np.array([10, 20, 30])
b = np.asarray(a)

print("Shares Memory:", np.shares_memory(a, b))