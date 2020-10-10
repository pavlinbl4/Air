n, m = map(int,input().split())
a =[]
for i in range(n):
    a.append(input().split())
for j in range(m):
    for i in range(n):
        print(a[i][j], end=" ")
    print()


