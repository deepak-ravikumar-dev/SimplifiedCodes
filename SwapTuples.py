# Swap elements of a tuple based on user input
tuple1 = tuple(input("Enter items for the first tuple separated by spaces: ").split())
tuple2 = tuple(input("Enter items for the second tuple separated by spaces: ").split())

# Swap the tuples
tuple1, tuple2 = tuple2, tuple1
print("Swapped tuple 1:", tuple1)
print("Swapped tuple 2:", tuple2)
