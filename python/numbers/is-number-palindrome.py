import sys

def is_palindrome(num):
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False

numbers = sys.argv

for count, num in enumerate(numbers):
    if count != 0:
        print "Is", num, "a palindrome? ", is_palindrome(num)