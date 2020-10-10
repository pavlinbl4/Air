n, m = map(int,input().split())
a = [] # исходный массив данных
for i in range(n):
    a.append(list(map(int,input().split())))
dd = []
for row in range(n):
    best = 0
    for colum in range(m):
        if a[row][colum] > best:
            best = a[row][colum]
    dd.append(best)
print(dd.count(max(dd)))