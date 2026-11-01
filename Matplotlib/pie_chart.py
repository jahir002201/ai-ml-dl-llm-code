import matplotlib.pyplot as plt

# Example: how a student's weekly study time is distributed.
activities = ["Programming", "Math", "English", "Revision"]
hours = [12, 8, 5, 5]

plt.figure(figsize=(7, 7))
plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.05, 0, 0, 0),
)
plt.title("Weekly Study Time Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()
