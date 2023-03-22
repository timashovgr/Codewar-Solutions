# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.
# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# note on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 
# ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

import math

def is_prime(num):

    if num<=1:
        return False
    
    if num>500:
        for i in range (2, (int(math.sqrt(num))+1)):
            if num%i == 0:
                return False
        return True
    
    if num<=500:
        for i in range (2, num):
            if num%i == 0:
                return False
        return True