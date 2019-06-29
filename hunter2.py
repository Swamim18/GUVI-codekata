l=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
c=0
for i in range(0,int(len(a))):
    c=(c*10)+a[i]
print(c)
