# Creating a dictionary
person = {
    "name": "Deepak",
    "age": 21,
    "city": "Bangalore"
}
print("Dictionary:", person)

# Accessing elements
print("Name:", person["name"])

# Adding and updating elements
person["email"] = "deepak@example.com"  # Add a new key-value pair
print("After add:", person)
person["age"] = 22                      # Update value
print("After update:", person)

# Dictionary methods
print("Keys:", person.keys())           # Get all keys
print("Values:", person.values())       # Get all values
print("Items:", person.items())         # Get all key-value pairs

# Loop through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
