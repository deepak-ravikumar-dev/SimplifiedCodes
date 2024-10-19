# Create a nested tuple from user input and access elements
nested_tuple = (
    tuple(map(int, input("Enter numbers for first group separated by spaces: ").split())),
    tuple(map(int, input("Enter numbers for second group separated by spaces: ").split()))
)
print("Nested Tuple:", nested_tuple)
