# Count the frequency of each character in a string entered by the user
text = input("Enter a string: ")
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Character frequency:", char_count)
