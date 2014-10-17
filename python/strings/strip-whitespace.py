# Strip Whitespace. Between words and at the beginning and end.
words = "This has the disadvantage\n that while you are in the\t loop"
remove = [" ", "\n", "\t"]
for item in remove:
    if item in words:
        words = words.replace(item, "")

print words