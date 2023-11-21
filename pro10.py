def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation number (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation number. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    calculator()