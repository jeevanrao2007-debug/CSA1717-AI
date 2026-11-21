def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
 
num = int(input("Enter a number: "))
print("Factorial of", num, "=", factorial(num))
print("Fibonacci series:", end=" ")
for i in range(num):
    print(fibonacci(i), end=" ")
print()
