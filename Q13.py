from math import sqrt
from itertools import count, islice

def isPrime(sw):
    if sw < 2:
        return False

    for number in islice(count(2), int(sqrt(sw) - 1)):
        if sw % number == 0:
            return False

    return True
sw=int(input())
if isPrime(sw):
    print("yes")
else:
    print("no")
