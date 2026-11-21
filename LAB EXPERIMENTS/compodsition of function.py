def add(a, b):
    return a + b
 
def square(n):
    return n * n
 
def double(n):
    return 2 * n
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
 
# Output of one function is the input of another
print("Square of sum   =", square(add(a, b)))
print("Double of square of sum =", double(square(add(a, b))))
