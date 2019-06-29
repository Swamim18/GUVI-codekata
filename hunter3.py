l=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if i==a[i]:
        b.append(i)
        
if len(b)>=1:
    print(*b)
else:
    print(-1)
