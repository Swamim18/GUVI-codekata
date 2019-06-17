from math import sqrt
from itertools import count, islice

def isPrime(sw):
    if sw < 2:
        return False

    for number in islice(count(2), int(sqrt(sw) - 1)):
        if sw % number == 0:
            return False

    return True
  
p,q=map(int,input().split())
a=[]
for i in range(p+1,q):
    if isPrime(i):
        a.append(i)
    
print(*a)
