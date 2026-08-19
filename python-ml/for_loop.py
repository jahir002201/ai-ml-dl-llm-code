# Basic for loop

for i in range(1, 6):
    print(i)

# List loop

names = ["Jahirul", "Rahim", "Karim"]

for name in names:
    print("Hello", name)

# Sum

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)

# Multiplication table

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
