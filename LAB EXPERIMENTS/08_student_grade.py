
mark = float(input("Enter student mark (0 to 100): "))

if mark < 0 or mark > 100:
    print("Invalid mark! Please enter a value between 0 and 100.")
elif mark >= 90:
    print("Grade: Grade A")
elif mark >= 80:
    print("Grade: Grade B")
elif mark >= 70:
    print("Grade: Grade C")
elif mark >= 60:
    print("Grade: Grade D")
else:
    print("Grade: Grade F")
