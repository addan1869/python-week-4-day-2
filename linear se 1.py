# Linear Search in a List

numbers = [12, 25, 18, 40, 33]

key = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Number found at index", i)
        found = True
        break

if not found:
    print("Number not found")