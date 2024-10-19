# Remove a specified key from a dictionary entered by the user
person = {
    "name": "Deepak",
    "age": "21",
    "city": "Bangalore",
    "occupation": "Student"
}
key_to_remove = input("Enter the key to remove from the dictionary: ")

if key_to_remove in person:
    del person[key_to_remove]
    print("Updated dictionary:", person)
else:
    print(f"The key '{key_to_remove}' was not found in the dictionary.")
