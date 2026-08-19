# List basics

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Indexing
print("First:", numbers[0])
print("Last:", numbers[-1])

# Change value
numbers[0] = 100
print("After change:", numbers)

# Add value
numbers.append(60)
print("After append:", numbers)

# Length
print("Length:", len(numbers))

# Membership
print(30 in numbers)

# Loop
for number in numbers:
    print(number)
