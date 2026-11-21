n = int(input("Enter the number of elements: "))
data = []
for i in range(n):
    data.append(int(input("Enter element: ")))
 
data.sort()
print("Sorted elements:", data)
 
print("Histogram:")
for x in data:
    print(f"{x:3} | " + "*" * x)
