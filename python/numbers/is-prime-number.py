import sys
import math

# Short Way
def is_prime(n):
    if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return True
    else:
        return False

# Long Way 

#def is_prime(n):
    # Make sure number is positive integer
#    n = abs(int(n))

    # Cannot be less than 2
#    if n < 2:
#        return False

    # 2 is the only even prime number
#    if n == 2:
#        return True

    # If it is an even number it is not prime.
#    if n % 2 == 0:
#        return False

    # Start at 3 and go up to given number.
    # The step is set to 2 to check every odd number.
#    for x in range(3, int(n)+1, 2):
#        print x
        # If there is no remainder than the number
        # might not be a prime number.
#        if n % x == 0:
            # If the number is itself continue.
#            if n == x:
#                continue

            # Else it is not a prime number.
#            return False

    # Return True if the number is prime.
#    return True

prime_numbers = sys.argv


for count, num in enumerate(prime_numbers):
    if count != 0:
        print "Is", num, "a prime number -", is_prime(int(num))
    count += 1