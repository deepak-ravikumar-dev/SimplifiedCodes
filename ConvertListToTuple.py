# Convert a list entered by the user to a tuple
my_list = input("Enter list items separated by spaces: ").split()
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)

# Convert tuple back to list
new_list = list(my_tuple)
print("List:", new_list)
