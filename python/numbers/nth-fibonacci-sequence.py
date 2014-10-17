# This returns the number at the given fibonacci sequence
import sys
import math

def fib(n):
    # Go here http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python to learn
    # about this formula.
    return round(int((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n) / (2**n * math.sqrt(5)))

nth_times = sys.argv
del nth_times[0]

for i, n in enumerate(nth_times):
    n = int(n)
    #fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
    print "\nFibonacci Number Sequenced", n, "times"
    print "%d" % fib(n)