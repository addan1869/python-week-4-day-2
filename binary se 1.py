# Binary Search

numbers = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Number found at index", mid)
        found = True
        break

    elif key < numbers[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Number not found")