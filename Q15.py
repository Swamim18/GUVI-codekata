p,q=map(int,input().split())
a=[]
for i in range(p+1,q):
    if (i%2==0):
        a.append(i)
print(*a)
