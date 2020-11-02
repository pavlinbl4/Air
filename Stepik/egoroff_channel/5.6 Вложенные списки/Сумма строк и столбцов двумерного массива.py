n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    print(sum(a[i]),end=" ")
print()
for j in range(m):
    stb = []
    for i in range(n):
        stb.append(a[i][j])
    print(sum(stb),end = ' ')
