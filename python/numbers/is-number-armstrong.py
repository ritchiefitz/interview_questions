# take input from the user
num = int(raw_input("Enter a number: "))

# initialise sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    print temp
    digit = temp % 10
    print digit
    sum += digit ** 3
    print temp
    temp //= 10

# display the result
if num == sum:
    print num, "is an Armstrong number"
else:
    print num, "is not an Armstrong number"