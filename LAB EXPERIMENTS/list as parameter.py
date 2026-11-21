def modify(lst):
    lst.append(100)          # lists are mutable, so the original changes
    lst[0] = 999
    print("Inside function:", lst)
 
def total(lst):
    s = 0
    for x in lst:
        s += x
    return s
 
numbers = [1, 2, 3, 4]
print("Before function:", numbers)
modify(numbers)
print("After function :", numbers)
print("Sum of list    :", total(numbers))
