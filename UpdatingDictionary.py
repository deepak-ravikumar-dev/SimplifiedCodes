# Update a dictionary with new key-value pairs entered by the user
person = {
    "name": "Deepak",
    "age": 21
}
key = input("Enter the key to update or add: ")
value = input("Enter the value: ")
person[key] = value
print("Updated dictionary:", person)
