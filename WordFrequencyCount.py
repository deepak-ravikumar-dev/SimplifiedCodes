# Count the frequency of each word in a user-entered string
sentence = input("Enter a sentence: ")
word_list = sentence.split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)
