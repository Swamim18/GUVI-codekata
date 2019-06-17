sw=input()
a=[]
for i in sw:
    a.append(i)
x=0
for i in range(len(a)):
    x=(int(a[i])**3)+x
sw=int(sw)
if x==sw:
    print("yes")
else:
    print("no")
