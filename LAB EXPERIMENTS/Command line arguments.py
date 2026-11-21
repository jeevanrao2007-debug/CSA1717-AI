import sys
 
print("Number of arguments:", len(sys.argv))
print("Script name        :", sys.argv[0])
print("Arguments          :", sys.argv[1:])
 
# Sum of the numbers given on the command line
total = 0
for arg in sys.argv[1:]:
    total += int(arg)
print("Sum of arguments   :", total)
 
# Run from the terminal as:
#   python prog27.py 10 20 30
