numbers = [5, 2, 8, 1, 9]

print("Original:", numbers)

numbers.append(10)
print("append:", numbers)

numbers.insert(1, 100)
print("insert:", numbers)

numbers.remove(100)
print("remove:", numbers)

removed = numbers.pop()
print("pop:", removed)
print("List:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

numbers.append(5)
print("count 5:", numbers.count(5))

print("index of 8:", numbers.index(8))

copied = numbers.copy()
print("copy:", copied)

copied.clear()
print("clear:", copied)
