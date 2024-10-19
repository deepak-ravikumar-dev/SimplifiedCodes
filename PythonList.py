# Creating a list
fruits = ['apple', 'banana', 'cherry']
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])     # Indexing
print("Last fruit:", fruits[-1])     # Negative indexing

# List operations
fruits.append('orange')              # Add an item to the end
print("After append:", fruits)
fruits.insert(1, 'mango')            # Insert at a specific index
print("After insert:", fruits)
fruits.remove('banana')              # Remove a specific item
print("After remove:", fruits)
fruits.pop()                         # Remove the last item
print("After pop:", fruits)

# List slicing
print("Slicing:", fruits[0:2])       # Get the first two items

# List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)
