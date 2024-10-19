# Find the longest word in a sentence entered by the user
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)
