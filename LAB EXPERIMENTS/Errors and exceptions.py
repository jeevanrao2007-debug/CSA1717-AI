try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("No exception occurred.")
finally:
    print("This block always executes.")
 
# File not found exception
try:
    f = open("nofile.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
 
# Raising an exception
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)
except ValueError as e:
    print("Error:", e)
