import matplotlib.pyplot as plt

# Example: monthly temperature trend.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperature = [18, 21, 25, 29, 31, 30]

plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker="o", linestyle="-", label="Temperature")
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
