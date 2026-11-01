import matplotlib.pyplot as plt

# Example: relationship between study hours and exam marks.
study_hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
marks = [35, 42, 50, 48, 60, 65, 68, 75, 82, 90]

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, marks, marker="o", label="Students")
plt.title("Study Hours vs Exam Marks")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
