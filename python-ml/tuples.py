# Tuple

numbers = (10, 20, 30, 40, 50)

print(numbers)

# Indexing

print(numbers[0])
print(numbers[-1])

# Slicing

print(numbers[1:4])

# Length

print("Length:", len(numbers))

# Count

numbers = (10, 20, 10, 30, 10)

print("Count:", numbers.count(10))

# Index

print("Index:", numbers.index(30))

# Unpacking

student = ("Jahirul", 20, "Python")

name, age, course = student

print(name)
print(age)
print(course)
