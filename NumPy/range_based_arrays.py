import numpy as np

# Example 1: arange()
arr1 = np.arange(10)
print("Arange:", arr1)

# Example 2: Start and Stop
arr2 = np.arange(1, 11)
print("Start Stop:", arr2)

# Example 3: Step
arr3 = np.arange(0, 20, 2)
print("Step:", arr3)

# Example 4: Negative Step
arr4 = np.arange(10, 0, -1)
print("Negative Step:", arr4)

# Example 5: Float Range
arr5 = np.arange(0, 5, 0.5)
print("Float Range:", arr5)

# Example 6: linspace()
arr6 = np.linspace(0, 10, 5)
print("Linspace:", arr6)

# Example 7: linspace() Endpoint False
arr7 = np.linspace(0, 10, 5, endpoint=False)
print("Endpoint False:", arr7)

# Example 8: Number of Samples
arr8 = np.linspace(1, 100, 10)
print("10 Samples:", arr8)

# Example 9: logspace()
arr9 = np.logspace(1, 3, 5)
print("Logspace:", arr9)

# Example 10: geomspace()
arr10 = np.geomspace(1, 1000, 4)
print("Geomspace:", arr10)

# Example 11: Reverse Range
arr11 = np.arange(20, 0, -2)
print("Reverse:", arr11)

# Example 12: Range to 2D
arr12 = np.arange(1, 13).reshape(3, 4)
print("2D Range:\n", arr12)