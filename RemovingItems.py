# Remove specific items from a set based on user input
my_set = set(input("Enter set items separated by spaces: ").split())
item_to_remove = input("Enter the item to remove from the set: ")

my_set.discard(item_to_remove)
print("Updated set:", my_set)
