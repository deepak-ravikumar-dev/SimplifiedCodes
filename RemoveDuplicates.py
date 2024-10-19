# Remove duplicates from a list entered by the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = list(set(numbers))
print("List with duplicates removed:", unique_numbers)
