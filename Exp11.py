def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # ... selection logic for Add, Subtract, Multiply, Divide ...