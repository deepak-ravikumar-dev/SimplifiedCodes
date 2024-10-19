# Check if one set is a subset or superset of another
set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())

print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))
