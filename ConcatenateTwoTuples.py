# Concatenate two tuples entered by the user
tuple1 = tuple(input("Enter items for the first tuple separated by spaces: ").split())
tuple2 = tuple(input("Enter items for the second tuple separated by spaces: ").split())
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
