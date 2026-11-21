def student(name, dept="CSE", year=1):
    print("Name:", name, "| Dept:", dept, "| Year:", year)
print("Positional:")
student("Arun", "ECE", 2)
print("Default:")
student("Bala")
print("Keyword:")
student(year=3, name="Charan", dept="IT")
