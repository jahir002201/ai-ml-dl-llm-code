text = "  Hello Python  "

print("Original:", text)

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())

print(
    "Replace:",
    text.replace("Python", "World")
)

text = "I love Python"

print("Find:", text.find("Python"))
print("Count:", text.count("o"))
print("Capitalize:", text.capitalize())
print("Title:", text.title())

print("Starts:", text.startswith("I"))
print("Ends:", text.endswith("Python"))

print("Split:", text.split())
