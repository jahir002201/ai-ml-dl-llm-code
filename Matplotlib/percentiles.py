import pandas as pd

marks = pd.Series([45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
                   72, 74, 75, 78, 80, 82, 85, 88, 90, 95])

print("25th percentile (Q1):", marks.quantile(0.25))
print("50th percentile (Median):", marks.quantile(0.50))
print("75th percentile (Q3):", marks.quantile(0.75))
print("90th percentile:", marks.quantile(0.90))

q1 = marks.quantile(0.25)
q3 = marks.quantile(0.75)
iqr = q3 - q1

print("Interquartile range (IQR):", iqr)
print("Lower fence:", q1 - 1.5 * iqr)
print("Upper fence:", q3 + 1.5 * iqr)
