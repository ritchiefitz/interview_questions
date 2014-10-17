import sys
import math

def list_primenumbers(num):

    print "\nAll Prime Numbers Under", num

    for n in range(1, num):

        if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
           print n



numbers = sys.argv
del numbers[0]

for i, num in enumerate(numbers):
    list_primenumbers(int(num))