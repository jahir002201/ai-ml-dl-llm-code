import matplotlib.pyplot as plt

# Compare marks across three departments.
cse = [65, 70, 72, 75, 80, 82, 85, 90, 95]
eee = [55, 60, 68, 70, 73, 78, 80, 84, 88]
bba = [60, 62, 65, 69, 72, 75, 77, 79, 83]

plt.figure(figsize=(8, 5))
plt.boxplot(
    [cse, eee, bba],
    tick_labels=["CSE", "EEE", "BBA"],
    showmeans=True,
)
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
