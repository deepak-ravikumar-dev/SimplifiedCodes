# Find the symmetric difference between two sets entered by the user
set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())

symmetric_difference = set1 ^ set2
print("Symmetric difference of sets:", symmetric_difference)
