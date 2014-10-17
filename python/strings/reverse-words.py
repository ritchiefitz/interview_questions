# Reverse Words in a string
words = "This has the disadvantage that while you are in the loop"
word_list = words.split(" ")
word_list_reversed = []

for word in reversed(word_list):
    word_list_reversed.append(word)

print word_list
print word_list_reversed