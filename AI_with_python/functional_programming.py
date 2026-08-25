def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))

print("Numbers:", numbers)
print("Squared:", squared_numbers)