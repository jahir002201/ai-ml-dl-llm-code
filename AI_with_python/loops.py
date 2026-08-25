print("for loop: ")

for i in range(5):
    print(i)

print("while loop: ")

count = 0
while count < 5:
    print(count)
    count += 1

print("nested loop: ")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")