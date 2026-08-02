numbers = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter Number: "))

print("\nLinear Search")

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")

print("\nBinary Search")

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Found at index", mid)
        break

    elif key < numbers[mid]:
        high = mid - 1

    else:
        low = mid + 1
else:
    print("Not Found")