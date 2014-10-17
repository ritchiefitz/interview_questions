import random
from random import shuffle

l_one = list(xrange(1,11))
l_two = list(xrange(1,11))

shuffle(l_two)

del l_two[random.randrange(1, 10)]

print l_one
print l_two

l_one = set(l_one)
l_two = set(l_two)
missing_num = list(l_one.difference(l_two))

print missing_num[0]

# for num in l_one:
#     if num not in l_two:
#         print "Number Missing: ", num
