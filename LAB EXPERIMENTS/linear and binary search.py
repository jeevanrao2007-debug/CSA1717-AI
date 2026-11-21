def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
 
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
 
arr = list(map(int, input("Enter numbers separated by space: ").split()))
key = int(input("Enter the element to search: "))
 
pos = linear_search(arr, key)
print("Linear search :", "Found at index " + str(pos) if pos != -1 else "Not found")
 
arr.sort()
print("Sorted list   :", arr)
pos = binary_search(arr, key)
print("Binary search :", "Found at index " + str(pos) if pos != -1 else "Not found")
