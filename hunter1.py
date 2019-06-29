l = int(input())
a = list(map(int,input().split()))
r = []
for i in range(len(a)):
    if a.count(a[i]) > 1:
        if a[i] not in r:
            r.append(a[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
