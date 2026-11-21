src = input("Enter the source file name: ")
dest = input("Enter the destination file name: ")
 
try:
    with open(src, "r") as f1, open(dest, "w") as f2:
        for line in f1:
            f2.write(line)
    print("File copied successfully.")
 
    # Display the copied content
    with open(dest, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: Source file not found.")
