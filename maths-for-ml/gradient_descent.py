# Minimize:
# f(x) = (x - 5)^2

x = 0.0
learning_rate = 0.1

for i in range(50):

    # derivative
    gradient = 2 * (x - 5)

    # gradient descent update
    x = x - learning_rate * gradient

    print(f"Iteration {i + 1}: x = {x:.6f}")

print("\nMinimum approximately at:", x)