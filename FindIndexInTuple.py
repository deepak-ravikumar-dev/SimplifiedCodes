# Find the index of an element in a tuple entered by the user
my_tuple = tuple(input("Enter tuple items separated by spaces: ").split())
element = input("Enter the element to find its index in the tuple: ")

if element in my_tuple:
    index = my_tuple.index(element)
    print(f"The index of {element} is {index}.")
else:
    print(f"{element} is not found in the tuple.")
