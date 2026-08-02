roll_numbers = [101, 102, 103, 104, 105, 106, 107, 108]

roll = int(input("Enter Roll Number: "))

low = 0
high = len(roll_numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if roll_numbers[mid] == roll:
        print("Roll Number Found at Index", mid)
        break

    elif roll < roll_numbers[mid]:
        high = mid - 1

    else:
        low = mid + 1
else:
    print("Roll Number Not Found")