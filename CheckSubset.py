# Check if one set is a subset of another set entered by the user
set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())

is_subset = set1.issubset(set2)
print(f"Is the first set a subset of the second set? {is_subset}")
