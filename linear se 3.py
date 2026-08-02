# Search Student Marks

marks = [75, 80, 65, 90, 88]

search = int(input("Enter marks to search: "))

for i in range(len(marks)):
    if marks[i] == search:
        print("Marks found at position", i)
        break
else:
    print("Marks not found")