import matplotlib.pyplot as plt

# Example: compare average marks across departments.
departments = ["CSE", "EEE", "BBA", "English"]
average_marks = [82, 88, 79, 85]

plt.figure(figsize=(8, 5))
bars = plt.bar(departments, average_marks, edgecolor="black")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

# Display each bar's value.
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1,
             f"{height:.0f}", ha="center")

plt.tight_layout()
plt.show()
