import numpy as np

# Generate random values
X = np.random.randint(1, 7, size=10000)

print("First 20 values:", X[:20])
print("Mean:", np.mean(X))
print("Variance:", np.var(X))
print("Standard deviation:", np.std(X))