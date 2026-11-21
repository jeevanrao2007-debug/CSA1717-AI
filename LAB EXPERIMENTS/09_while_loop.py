
n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print("Numbers from 1 to", n, "using while loop:")
    i = 1
    while i <= n:
        print(i)
        i = i + 1
