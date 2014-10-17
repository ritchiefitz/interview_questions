# Find the number that is enterd in only twice
# This solution works if numbers are in order.
import random
max_num = 1001
array = list(xrange(1, max_num))
array[random.randrange(1, max_num)] = random.randrange(1, max_num)

prev = 0
temp = 0
count = 0
for num in array:
    if temp > num:
        print "Number: ", num
        print "Temp: ", temp
        print "Prev: ", prev
        if prev + 1 == temp:
            print "Answer: ", num
        else:
            print "Answer: ", temp


    prev = temp
    temp = num
    count += 1

print array
