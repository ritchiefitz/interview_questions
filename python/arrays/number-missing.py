# Find the number that is missing
# This solution works if numbers are in order.
import random
max_num = 1001
array = list(xrange(1, max_num))
del array[random.randrange(1, max_num)]

temp = 0
for num in array:
    if temp+1 != num:
        print "Number: ", num
        print "Temp: ", temp
        print "Answer: ", num-1

    temp = num

print array