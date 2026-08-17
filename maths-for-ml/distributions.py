import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(
    loc=0,
    scale=1,
    size=10000
)

plt.hist(data, bins=50)

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()