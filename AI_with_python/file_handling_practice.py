filename = "students_practice.txt"

students = [
    "Jahirul",
    "Rahim",
    "Karim",
    "Hasan"
]

with open(filename, "w") as file:
    for student in students:
        file.write(student + "\n")


with open(filename, "r") as file:
    data = file.readlines()


print("Students:")

for student in data:
    print(student.strip())