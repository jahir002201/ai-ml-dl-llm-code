import sympy as sp

x = sp.symbols("x")

f = x**3 + 2*x**2 + 5*x

derivative = sp.diff(f, x)

print("Function:")
print(f)

print("\nDerivative:")
print(derivative)