import numpy as np

scalar = 5

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Scalar:", scalar)
print("Vector 1:", v1)
print("Vector 2:", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Scalar multiplication:", scalar * v1)
print("Dot product:", np.dot(v1, v2))
print("Vector norm:", np.linalg.norm(v1))