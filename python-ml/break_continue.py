# break

for i in range(1, 11):
    if i == 6:
        break

    print(i)

print("---")

# continue

for i in range(1, 11):
    if i == 5:
        continue

    print(i)

print("---")

# Find a number

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found:", number)
        break
