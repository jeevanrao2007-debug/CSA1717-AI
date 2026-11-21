num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("\n--- Arithmetic Operations Results ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
    print("Division:", division)
    print("Modulus:", modulus)
else:
    print("Division: Cannot divide by zero.")
    print("Modulus: Cannot compute modulus with zero divisor.")
