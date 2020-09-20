n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    empty=[]
    for j in range(m-1,-1,-1):
        empty.append(a[i][j])
    print(*empty)




