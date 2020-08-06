a = []
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n-1,-1,-1):
    ss = []
    for j in range(n - 1, -1, -1):
        ss.append(a[j][i])
    print(*ss)
