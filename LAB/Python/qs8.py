import sys

# Get the command-line arguments
numbers = sys.argv[1:]

# Display all elements
print("All elements:")
for i in range(len(numbers)):
    print(numbers[i])

print("hoi")

# Display elements in even positions
print("\nElements in even positions:")
for i in range(0, len(numbers), 2):
    print(numbers[i])

# Display elements in odd positions
print("\nElements in odd positions:")
for i in range(1, len(numbers), 2):
    print(numbers[i])