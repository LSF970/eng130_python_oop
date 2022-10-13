# Simple OOP Calculator

# Addition
def add(int1, int2):
    return int1 + int2

# Subtraction
def subtract(int1, int2):
    return int1 - int2

# Multiplication
def multiply(int1, int2):
    return int1 * int2

# Division
def divide(int1, int2):
    return int1 / int2

# Modulo
def modulo(int1, int2):
    return int1 % int2

print("Addition")
print(add(int(input("Please enter first number")), int(input("Please enter second number"))))

print("Subtraction")
print(subtract(int(input("Please input first number")), int(input("Please enter second number"))))

print("Multiplication")
print(multiply(int(input("Please input first number")), int(input("Please enter second number"))))

print("Division")
print(divide(int(input("Please input first number")), int(input("Please enter second number"))))

print("Modulous")
print(modulo(int(input("Please input first number")), int(input("Please enter second number"))))