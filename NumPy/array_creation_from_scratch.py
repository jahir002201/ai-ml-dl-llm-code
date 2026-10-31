import numpy as np

# Example 1: zeros()
arr1 = np.zeros(5)
print("Zeros:", arr1)

# Example 2: ones()
arr2 = np.ones(5)
print("Ones:", arr2)

# Example 3: full()
arr3 = np.full(5, 7)
print("Full:", arr3)

# Example 4: empty()
arr4 = np.empty(5)
print("Empty:", arr4)

# Example 5: zeros() 2D
arr5 = np.zeros((3, 3))
print("2D Zeros:\n", arr5)

# Example 6: ones() 2D
arr6 = np.ones((2, 4))
print("2D Ones:\n", arr6)

# Example 7: full() 2D
arr7 = np.full((2, 3), 10)
print("2D Full:\n", arr7)

# Example 8: eye()
arr8 = np.eye(3)
print("Eye:\n", arr8)

# Example 9: identity()
arr9 = np.identity(4)
print("Identity:\n", arr9)

# Example 10: zeros_like()
original = np.array([10, 20, 30])
arr10 = np.zeros_like(original)
print("Zeros Like:", arr10)

# Example 11: ones_like()
arr11 = np.ones_like(original)
print("Ones Like:", arr11)

# Example 12: full_like()
arr12 = np.full_like(original, 99)
print("Full Like:", arr12)

# Example 13: Triangular Matrix
arr13 = np.tri(3, 3)
print("Triangle:\n", arr13)

# Example 14: Diagonal Matrix
arr14 = np.diag([1, 2, 3])
print("Diagonal:\n", arr14)