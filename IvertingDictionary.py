# Invert a dictionary (swap keys and values) entered by the user
original_dict = {}
n = int(input("Enter the number of key-value pairs: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    original_dict[key] = value

inverted_dict = {value: key for key, value in original_dict.items()}
print("Inverted dictionary:", inverted_dict)
