student = {
    "name": "Jahirul",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print(student)

# Access

print("Name:", student["name"])
print("Age:", student.get("age"))

# Keys

print("Keys:", student.keys())

# Values

print("Values:", student.values())

# Items

print("Items:", student.items())

# Add

student["city"] = "Mymensingh"

print("After add:", student)

# Update

student["marks"] = 90

print("After update:", student)

# Pop

removed = student.pop("city")

print("Removed:", removed)
print("Student:", student)

# Loop

for key, value in student.items():
    print(key, ":", value)
