# Write mode ('w') creates the file or overwrites it
f = open("sample.txt", "w")
f.write("Welcome to Python programming.")
f.write("This is a file handling example.")
f.close()
print("Content written successfully.")
 
# Append mode ('a') adds to the end of the file
with open("sample.txt", "a") as f:
    f.write("This line is appended.")
print("Content appended successfully.")
 
# Display the file content
with open("sample.txt", "r") as f:
    print(f.read())
