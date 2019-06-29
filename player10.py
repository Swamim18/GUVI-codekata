p,q=map(str,input().split())
count=0
for i in range(len(p)):
    if p[i]==q[i]:
        count+=1
        
if len(p)-count==1:
    print("yes")
else:
    print("no")
