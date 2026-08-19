# Basic dictionary comprehension

numbers = {
    i: i ** 2
    for i in range(1, 6)
}

print(numbers)

# Even numbers

even_numbers = {
    i: i ** 2
    for i in range(1, 11)
    if i % 2 == 0
}

print(even_numbers)

# Names and lengths

names = ["Jahirul", "Rahim", "Karim"]

name_lengths = {
    name: len(name)
    for name in names
}

print(name_lengths)
