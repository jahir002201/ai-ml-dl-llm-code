class Me:
    pass

me = Me()

me.name = "Jahirul Islam"
me.age = 26

me.department = "Mathematics"
me.university = "National University of Bangladesh"

me.stack = ["django", "fastapi", "laravel", "sql", "reactjs", "nextjs"]

me.city = "Dhaka"
me.country = "Bangladesh"

print(me.name)
print(me.stack)

# iterating through the object
print("Iterating through the object:")
for attr in dir(me):
    if not attr.startswith("__"):
        print(f"{attr}: {getattr(me, attr)}")