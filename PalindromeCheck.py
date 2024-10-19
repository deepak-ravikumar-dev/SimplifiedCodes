# Check if a string entered by the user is a palindrome
text = input("Enter a word to check if it's a palindrome: ")
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
