# Remove vowels from a string entered by the user
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowel_text = "".join([char for char in text if char not in vowels])
print("String without vowels:", no_vowel_text)
