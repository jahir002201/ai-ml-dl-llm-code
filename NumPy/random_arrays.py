import numpy as np

# Example 1: Random Float
arr1 = np.random.rand(5)
print("Random Float:", arr1)

# Example 2: Random 2D Array
arr2 = np.random.rand(2, 3)
print("Random 2D:\n", arr2)

# Example 3: Random Integer
arr3 = np.random.randint(1, 100, size=5)
print("Random Integer:", arr3)

# Example 4: Random Integer 2D
arr4 = np.random.randint(1, 50, size=(3, 3))
print("Random Integer 2D:\n", arr4)

# Example 5: Standard Normal Distribution
arr5 = np.random.randn(5)
print("Random Normal:", arr5)

# Example 6: Normal Distribution
arr6 = np.random.normal(50, 10, size=5)
print("Normal Distribution:", arr6)

# Example 7: Random Choice
arr7 = np.random.choice([10, 20, 30, 40], size=3)
print("Choice:", arr7)

# Example 8: Random Shuffle
arr8 = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr8)
print("Shuffle:", arr8)

# Example 9: Random Permutation
arr9 = np.random.permutation([1, 2, 3, 4, 5])
print("Permutation:", arr9)

# Example 10: Random Seed
np.random.seed(42)
arr10 = np.random.randint(1, 100, size=5)
print("Seed:", arr10)

# Example 11: Modern Random Generator
rng = np.random.default_rng(42)

arr11 = rng.integers(1, 100, size=5)
print("Default RNG:", arr11)

# Example 12: Random Boolean
arr12 = rng.choice([True, False], size=5)
print("Random Boolean:", arr12)

# Example 13: Random Bytes
arr13 = rng.bytes(5)
print("Random Bytes:", arr13)