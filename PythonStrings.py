# Creating a string
text = "Hello, World!"
print("String:", text)

# String operations
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("World", "Python"))
print("Split:", text.split(','))

# String slicing
print("First 5 characters:", text[:5])
print("Last 6 characters:", text[-6:])

# String formatting
name = "Deepak"
age = 21
print(f"My name is {name} and I am {age} years old.")  # f-string
