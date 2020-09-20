n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n-1,-1,-1):
    empty = []
    for j in range(m):
        empty.append(a[i][j])
    print(*empty)
