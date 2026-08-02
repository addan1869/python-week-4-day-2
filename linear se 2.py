# Linear Search for Student Names

students = ["Ali", "Ahmed", "Usman", "Hamza", "Ayan"]

name = input("Enter student name: ")

found = False

for i in range(len(students)):
    if students[i].lower() == name.lower():
        print("Student found at index", i)
        found = True
        break

if not found:
    print("Student not found")