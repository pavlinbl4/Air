n = 5
a = []
for x in range(n):
    a.append(list(map(int,input().split())))
for x in range(n):
    if 1 in a[x]:
        i = x +1
        j = a[x].index(1) +1
print(abs(3-j) + abs(3- i))