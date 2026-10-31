import numpy as np

# Example 1: Matrix Creation
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:\n", a)
print("Matrix B:\n", b)

# Example 2: Matrix Addition
print("Addition:\n", a + b)

# Example 3: Matrix Subtraction
print("Subtraction:\n", a - b)

# Example 4: Element-wise Multiplication
print("Multiplication:\n", a * b)

# Example 5: Matrix Division
print("Division:\n", a / b)

# Example 6: Dot Product
print("Dot Product:\n", np.dot(a, b))

# Example 7: Matrix Multiplication
print("Matrix Multiplication:\n", a @ b)

# Example 8: Transpose
print("Transpose:\n", a.T)

# Example 9: Determinant
print("Determinant:", np.linalg.det(a))

# Example 10: Inverse
print("Inverse:\n", np.linalg.inv(a))

# Example 11: Matrix Rank
print("Rank:", np.linalg.matrix_rank(a))

# Example 12: Trace
print("Trace:", np.trace(a))

# Example 13: Diagonal
print("Diagonal:", np.diag(a))

# Example 14: Solve Linear Equations
A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([5, 6])

solution = np.linalg.solve(A, B)

print("Solution:", solution)

# Example 15: Eigenvalues
values = np.linalg.eigvals(a)

print("Eigenvalues:", values)

# Example 16: Eigenvalues and Eigenvectors
values, vectors = np.linalg.eig(a)

print("Eigenvalues:\n", values)
print("Eigenvectors:\n", vectors)

# Example 17: Matrix Norm
print("Matrix Norm:", np.linalg.norm(a))

# Example 18: Vector Norm
vector = np.array([3, 4])
print("Vector Norm:", np.linalg.norm(vector))

# Example 19: Singular Value Decomposition
U, S, VT = np.linalg.svd(a)

print("U:\n", U)
print("S:\n", S)
print("VT:\n", VT)

# Example 20: Matrix Power
print("Matrix Power:\n", np.linalg.matrix_power(a, 2))

# Example 21: QR Decomposition
Q, R = np.linalg.qr(a)

print("Q:\n", Q)
print("R:\n", R)

# Example 22: Least Squares
x = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
])

y = np.array([2, 3, 4])

result = np.linalg.lstsq(x, y, rcond=None)

print("Least Squares:", result[0])