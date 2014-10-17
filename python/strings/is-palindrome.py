# Checks to see if string is palindrome.
import sys

cmd_line = sys.argv
string = cmd_line[1]

copy_string = string[::-1]

if string == copy_string:
    print string, " is a palindrome"
else:
    print copy_string, " is not a palindrome"
