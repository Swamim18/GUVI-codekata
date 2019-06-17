sw,sa=map(int,input().split())
for i in range (sw+1,sa):
    z=0
    p=i
    while(p>0):
        x=p%10
        p=p//10
        y=x**3
        z=z+y
    if(i==z):
        print(z,end=' ')
