# Goes through each number.
import sys

def floor_divide(num):
    print num
    while num > 0:
        # Gets the last number.
        digit = num % 10
        print digit
        # Removes the last number.
        num //= 10

numbers = sys.argv
del numbers[0]

for i, num in enumerate(numbers):
    floor_divide(int(num))