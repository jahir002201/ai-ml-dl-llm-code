# add
def add(a, b):
    return a + b

# subtract
def subtract(a, b):
    return a - b

# multiply
def multiply(a, b):
    return a * b

# divide
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# modulus
def modulus(a, b):
    return a % b

# exponent
def exponent(a, b):
    return a ** b

# floor division
def floor_division(a, b):
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b

# bitmask operations
def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def bitwise_not(a):
    return ~a

print("Functions :")
print("add(2, 3) :", add(2, 3))