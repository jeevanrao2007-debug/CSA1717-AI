# Make sure sample.txt exists (it is created by program 26)
f = open("dictionary.py", "r")
 
print("Using read():")
print(f.read())
f.close()
 
print("Using readline():")
f = open("sample.txt", "r")
print(f.readline())
f.close()
 
print("Using readlines():")
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)
 
print("Reading line by line:")
with open("sample.txt", "r") as f:
    for line in f:
        print(line, end="")
