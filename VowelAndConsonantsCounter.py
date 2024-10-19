# Count the number of vowels and consonants in a string entered by the user
text = input("Enter a sentence: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
