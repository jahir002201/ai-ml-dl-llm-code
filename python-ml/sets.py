# Set

numbers = {1, 2, 3, 4, 5}

print(numbers)

# Duplicate values

numbers = {1, 2, 2, 3, 3, 4}

print("Duplicates removed:", numbers)

# Add

numbers.add(10)
print("After add:", numbers)

# Remove

numbers.remove(10)
print("After remove:", numbers)

# Union

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)

# Intersection

print("Intersection:", a & b)

# Difference

print("Difference:", a - b)

# Membership

print(2 in a)
