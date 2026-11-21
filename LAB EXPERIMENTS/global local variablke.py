x = 10          # global variable
 
def display():
    y = 20      # local variable
    print("Inside function: x =", x, ", y =", y)
 
def modify():
    global x
    x = x + 5   # modifies the global variable
    z = 1       # local variable
    print("Inside modify: x =", x, ", z =", z)
 
display()
modify()
print("Outside function: x =", x)
# print(y)  # Error: y is local to display()
