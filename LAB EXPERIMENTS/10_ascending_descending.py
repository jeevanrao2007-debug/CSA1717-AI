n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print("\nAscending order (1 to " + str(n) + "):")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

    print("\nDescending order (" + str(n) + " to 1):")
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()
