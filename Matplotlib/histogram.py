import matplotlib.pyplot as plt

# Example: distribution of exam marks.
marks = [45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

plt.figure(figsize=(8, 5))
plt.hist(marks, bins=6, edgecolor="black")
plt.title("Distribution of Exam Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
