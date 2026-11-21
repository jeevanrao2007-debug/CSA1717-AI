student = {"name": "Arun", "dept": "CSE", "year": 2}
print("Dictionary:", student)
 
student["mark"] = 85                 # add a new key
student["year"] = 3                  # update a value
print("After add/update:", student)
 
print("Value of name :", student["name"])
print("Using get()   :", student.get("age", "Not found"))
print("Keys          :", list(student.keys()))
print("Values        :", list(student.values()))
print("Items         :", list(student.items()))
 
student.pop("dept")                  # delete a key
print("After pop     :", student)
print("'name' in dict:", "name" in student)
 
for k, v in student.items():
    print(k, "->", v)
 
student.clear()
print("After clear   :", student)
