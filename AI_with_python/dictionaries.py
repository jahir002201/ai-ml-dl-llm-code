me = {
    "name": "Jahirul Islam",
    "age": 26,
    "department": "Mathematics",
    "university": "National University of Bangladesh",
    "stack": ["django", "fastapi", "laravel", "sql", "reactjs", "nextjs"],
    "city": "Dhaka",
    "country": "Bangladesh"
}

print(me["name"])

print(me["age"])

print(me["department"])

print(me["university"])

print(me["stack"])


# iterating through the dictionary
print("Iterating through the dictionary:")

for key, value in me.items():
    print(f"{key}: {value}")