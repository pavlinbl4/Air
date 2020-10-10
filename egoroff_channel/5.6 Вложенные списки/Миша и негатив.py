n,m = map(int,input().split())
a = []
b = []
for i in range(n):
        a.append([x for x in input()])
if input() != 0:
    for i in range(n):
            b.append([x for x in input()])
count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1
print(count)
