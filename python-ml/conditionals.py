# Simple condition

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Grade system

marks = 85

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "Fail"

print("Grade:", grade)

# Condition inside loop

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number, "Even")
    else:
        print(number, "Odd")
