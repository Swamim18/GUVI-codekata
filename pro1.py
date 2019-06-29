l=int(input())
b=[]
for i in range(0,l):
    inp=input()
    b.append(inp)
li=[]
for i in zip(*b):
    if(i.count(i[0])==len(i)):
        li.append(i[0])
            
    else:
        break
print(''.join(li))
