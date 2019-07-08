def find_sum(arr, x):
    a2 = 0
    for i in arr:
        if(i < x):
            a2 += i
    return a2

N = int(input())
arr = list(map(int, input().split()))
a = 0
for i in range(N):
    a += find_sum(arr[:i+1], arr[i])

print(a)
