a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))
print("\nBefore circulating:")
print("a =", a, ", b =", b, ", c =", c)
temp = c
c = b
b = a
a = temp
print("\nAfter circulating:")
print("a =", a, ", b =", b, ", c =", c)
