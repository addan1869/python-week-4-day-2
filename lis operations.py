# Common Array/List Operations in Python

# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Access elements
print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])

# Update an element
numbers[2] = 35
print("\nAfter Updating:", numbers)

# Append a new element
numbers.append(60)
print("After Append:", numbers)

# Insert an element
numbers.insert(1, 15)
print("After Insert:", numbers)

# Remove an element by value
numbers.remove(40)
print("After Remove:", numbers)

# Delete an element by index
del numbers[0]
print("After Delete:", numbers)

# Find the length
print("\nLength of List:", len(numbers))

# Sort the list
numbers.sort()
print("Sorted List:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed List:", numbers)

# Search for an element
key = int(input("\nEnter a number to search: "))

if key in numbers:
    print(key, "is found in the list.")
else:
    print(key, "is not found in the list.")

# Count occurrences
print("\nCount of 20:", numbers.count(20))

# Find maximum and minimum
print("Maximum Number:", max(numbers))
print("Minimum Number:", min(numbers))

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)