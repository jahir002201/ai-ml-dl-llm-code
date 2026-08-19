# Numbers

numbers = [i for i in range(1, 11)]
print("Numbers:", numbers)

# Squares

squares = [i ** 2 for i in range(1, 11)]
print("Squares:", squares)

# Even numbers

even_numbers = [
    i for i in range(1, 21)
    if i % 2 == 0
]

print("Even:", even_numbers)

# Odd numbers

odd_numbers = [
    i for i in range(1, 21)
    if i % 2 != 0
]

print("Odd:", odd_numbers)

# Strings

names = ["jahirul", "rahim", "karim"]

upper_names = [
    name.upper()
    for name in names
]

print("Upper:", upper_names)

# String lengths

lengths = [
    len(name)
    for name in names
]

print("Lengths:", lengths)
