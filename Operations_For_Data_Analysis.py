# Perform set operations based on user inputs
set_a = set(input("Enter elements of the first set separated by spaces: ").split())
set_b = set(input("Enter elements of the second set separated by spaces: ").split())
print("Union:", set_a | set_b)                    # All elements from both sets
print("Difference:", set_a - set_b)              # Elements in set_a not in set_b
print("Symmetric Difference:", set_a ^ set_b)    # Elements in either set, but not both
