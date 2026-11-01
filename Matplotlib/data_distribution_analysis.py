import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example dataset: exam marks of 20 students.
marks = pd.Series([
    45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
    72, 74, 75, 78, 80, 82, 85, 88, 90, 95
], name="Marks")

# Percentiles describe the position of values in a distribution.
percentiles = marks.quantile([0.25, 0.50, 0.75, 0.90])

print("Distribution summary:")
print(marks.describe())

print("\nSelected percentiles:")
print(percentiles.rename({
    0.25: "25th percentile (Q1)",
    0.50: "50th percentile (Median)",
    0.75: "75th percentile (Q3)",
    0.90: "90th percentile",
}))

print("\nInterquartile range (IQR):", marks.quantile(0.75) - marks.quantile(0.25))

# Draw a histogram and a boxplot in separate figures.
plt.figure(figsize=(8, 5))
plt.hist(marks, bins=6, edgecolor="black")
plt.title("Exam Marks: Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.boxplot(marks, orientation="horizontal", showmeans=True)
plt.title("Exam Marks: Boxplot")
plt.xlabel("Marks")
plt.tight_layout()
plt.show()
