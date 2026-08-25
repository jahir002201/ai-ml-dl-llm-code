numbers = [1, 2, 3, 4, 5]
print("List of numbers: ", numbers)

numbers.append(6)
print("After appending 6: ", numbers)

numbers.remove(3)
print("After removing 3: ", numbers)

print("Length of the list: ", len(numbers))

print("Iterating through the list:")
for num in numbers:
    print(num)

print("Slicing the list: ", numbers[1:4])

print("Reversing the list: ", numbers[::-1])

print("Sorting the list: ", sorted(numbers))

print("First element: ", numbers[0])
print("Last element: ", numbers[-1])