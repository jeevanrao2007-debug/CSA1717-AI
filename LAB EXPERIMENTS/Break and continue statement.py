x = 10          
def display():
    y = 20      
    print("Inside function: x =", x, ", y =", y)
def modify():
    global x
    x = x + 5   
    z = 1       
    print("Inside modify: x =", x, ", z =", z)
display()
modify()
print("Outside function: x =", x)
