l, r = map(int, input().split())
def prime_check(n):
    if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               return False
               break
       else:
           return True
    else:
       return False
       
prime_list = list(filter(prime_check,range(l, r+1)))
print(len(prime_list))
