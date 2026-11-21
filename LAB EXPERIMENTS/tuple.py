t = (10, 20, 30, 40, 50)
print("Tuple        :", t)
print("First element:", t[0])
print("Slice [1:4]  :", t[1:4])
print("Length       :", len(t))
print("Max / Min    :", max(t), "/", min(t))
print("Count of 20  :", t.count(20))
print("Index of 30  :", t.index(30))
 
t2 = (60, 70)
print("Concatenation:", t + t2)
print("Repetition   :", t2 * 2)
 
# Tuple packing and unpacking
a, b, c, d, e = t
print("Unpacked     :", a, b, c, d, e)
 
# Tuples are immutable
# t[0] = 5   # Error: 'tuple' object does not support item assignment
