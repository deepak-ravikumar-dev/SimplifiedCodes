# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple operations
print("Length of tuple:", len(my_tuple))
print("Count of 3 in tuple:", my_tuple.count(3))
print("Index of 4 in tuple:", my_tuple.index(4))

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
