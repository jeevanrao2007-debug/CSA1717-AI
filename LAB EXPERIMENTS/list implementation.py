fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
 
fruits.append("mango")           # add at end
fruits.insert(1, "orange")       # add at index
print("After append/insert:", fruits)
 
fruits.remove("banana")          # remove by value
last = fruits.pop()              # remove last item
print("After remove/pop:", fruits, "| popped:", last)
 
fruits.sort()
print("Sorted:", fruits)
fruits.reverse()
print("Reversed:", fruits)
 
print("Length:", len(fruits))
print("Index of cherry:", fruits.index("cherry"))
print("Slice [0:2]:", fruits[0:2])
