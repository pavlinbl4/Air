# n, m = map(int,input().split())
n = 4
m = 10
a = []
k = 0
dd = m
for i in range(n):
    ss = [x for x in range(k, m)]
    k += dd
    m += dd
    if i%2 == 0:
        a.append(ss)
    else:
        ss.reverse()
        a.append(ss)
for i in range(n):
    print()
    for j in range(dd):
        if a[i][j] < 10:
            print(a[i][j],end="  ")
        else:
            print("",a [i] [j], end="")