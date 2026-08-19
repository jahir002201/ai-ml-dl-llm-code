"""
How a Machine Learning Model Works

1. Collect data
2. Prepare data
3. Split data
4. Train model
5. Make predictions
6. Evaluate model
"""

data = [
    [1, 40],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
]

print("Dataset:")

for row in data:
    print(row)

# Separate features and targets

X = []
y = []

for row in data:
    X.append(row[0])
    y.append(row[1])

print()
print("Features:", X)
print("Targets:", y)

# Simple prediction example

new_hours = 6

predicted_score = 90

print()
print("New study hours:", new_hours)
print("Predicted score:", predicted_score)

print()
print("Machine Learning workflow:")
print("1. Collect data")
print("2. Clean data")
print("3. Prepare data")
print("4. Train model")
print("5. Predict")
print("6. Evaluate")
