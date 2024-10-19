# Merge two dictionaries based on user input
dict1 = {}
dict2 = {}
for i in range(2):
    key = input(f"Enter key for dictionary 1, item {i+1}: ")
    value = input(f"Enter value for dictionary 1, item {i+1}: ")
    dict1[key] = value

for i in range(2):
    key = input(f"Enter key for dictionary 2, item {i+1}: ")
    value = input(f"Enter value for dictionary 2, item {i+1}: ")
    dict2[key] = value

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)
