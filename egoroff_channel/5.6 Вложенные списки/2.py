a = []
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    empty=[]
    for j in range(n):
        empty.append(a[j][i])
    print(*empty)
