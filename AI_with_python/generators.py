def number_generator(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


for number in number_generator(5):
    print(number)