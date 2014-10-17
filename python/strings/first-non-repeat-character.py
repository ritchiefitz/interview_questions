# Find the first non repeating character
import time

word = "AAABBBCCCDDDEEEFFFGHHIIIIII"

start2 = time.clock()
checked = []
for char in word:
    if char in checked:
        continue
    occur = word.count(char)
    if occur == 1:
        print char
        break
    checked.append(char)
end2 = time.clock()

print end2 - start2