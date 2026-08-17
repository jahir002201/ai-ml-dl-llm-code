import sympy as sp

x = sp.symbols("x")

# f(x) = sin(x^2)
f = sp.sin(x**2)

derivative = sp.diff(f, x)

print("f(x) =", f)
print("f'(x) =", derivative)