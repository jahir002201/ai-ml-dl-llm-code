import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("A + B:")
print(A + B)

print("\nA @ B:")
print(A @ B)

print("\nTranspose:")
print(A.T)

print("\nDeterminant:")
print(np.linalg.det(A))

print("\nInverse:")
print(np.linalg.inv(A))