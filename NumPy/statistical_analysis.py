import numpy as np

marks = np.array([70, 80, 90, 60, 100])

# Example 1: sum()
print("Sum:", np.sum(marks))

# Example 2: mean()
print("Mean:", np.mean(marks))

# Example 3: median()
print("Median:", np.median(marks))

# Example 4: Standard Deviation
print("Standard Deviation:", np.std(marks))

# Example 5: Variance
print("Variance:", np.var(marks))

# Example 6: Minimum
print("Minimum:", np.min(marks))

# Example 7: Maximum
print("Maximum:", np.max(marks))

# Example 8: Percentile
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

# Example 9: Cumulative Sum
print("Cumsum:", np.cumsum(marks))

# Example 10: Cumulative Product
print("Cumprod:", np.cumprod(np.array([1, 2, 3, 4])))

# Example 11: Product
print("Product:", np.prod(np.array([2, 3, 4])))

# Example 12: Average
print("Average:", np.average(marks))

# Example 13: Weighted Average
scores = np.array([80, 90, 70])
weights = np.array([0.2, 0.5, 0.3])

print("Weighted Average:", np.average(scores, weights=weights))

# Example 14: Correlation
x = np.array([10, 20, 30, 40, 50])
y = np.array([20, 40, 60, 80, 100])

print("Correlation:\n", np.corrcoef(x, y))

# Example 15: Covariance
print("Covariance:\n", np.cov(x, y))

# Example 16: Histogram
data = np.array([10, 20, 20, 30, 30, 30, 40, 50])

hist, bins = np.histogram(data, bins=5)

print("Histogram:", hist)
print("Bins:", bins)

# Example 17: Axis Based Mean
data = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 100]
])

print("Row Mean:", np.mean(data, axis=1))
print("Column Mean:", np.mean(data, axis=0))

# Example 18: Axis Based Sum
print("Row Sum:", np.sum(data, axis=1))
print("Column Sum:", np.sum(data, axis=0))

# Example 19: Conditional Statistics
passed = marks[marks >= 70]

print("Passed Marks:", passed)
print("Passed Average:", np.mean(passed))

# Example 20: NaN Handling
data = np.array([10, 20, np.nan, 40, 50])

print("Normal Mean:", np.mean(data))
print("NaN Safe Mean:", np.nanmean(data))
print("NaN Safe Sum:", np.nansum(data))