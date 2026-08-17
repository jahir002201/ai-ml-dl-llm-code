import numpy as np

# 2x + 3y = 8
# x - y = 1

A = np.array([
    [2, 3],
    [1, -1]
])

b = np.array([8, 1])

solution = np.linalg.solve(A, b)

print("x =", solution[0])
print("y =", solution[1])