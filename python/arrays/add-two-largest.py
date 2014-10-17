# Add two largest numbers in array
import random
max_num = 10
n = 4
array = [random.randrange(1, max_num) for x in range(0, 10)]
array.sort()
print array

sum_num = 0

while n:
    largest = max(array)
    del array[array.index(max(array))]
    sum_num = sum_num + largest
    n -= 1

print array
print sum_num