# split()

text = "Python,Machine,Learning"

items = text.split(",")

print("Split:", items)

# join()

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print("Join:", sentence)

# f-string

name = "Jahirul"
age = 20

message = f"My name is {name} and I am {age} years old."

print(message)

# format()

message = "My name is {} and I am {} years old."

print(message.format(name, age))

# Number formatting

price = 99.9999

print(f"Price: {price:.2f}")
