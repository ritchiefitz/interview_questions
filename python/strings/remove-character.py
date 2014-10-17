import sys

def remove_character(word, character):
        return word.replace(character, "")


words = sys.argv

character = words[1]

print "\nCharacter to be Removed: ", character

for count, word in enumerate(words):
    if count != 0 and count != 1:
        print "Original String: ", word
        print "Removed Character: ", remove_character(word, character)
    count += 1