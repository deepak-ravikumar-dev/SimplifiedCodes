# Check if a specific element exists in a tuple
my_tuple = tuple(input("Enter tuple items separated by spaces: ").split())
element = input("Enter the element to check: ")
if element in my_tuple:
    print(f"{element} is in the tuple.")
else:
    print(f"{element} is not in the tuple.")
