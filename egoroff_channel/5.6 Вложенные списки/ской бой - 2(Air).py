n, m = map(int,input().split())
a = []
a.append(["@" for x in range(m + 2)])
for i in range(n):
    z = [x for x in input()]
    z.insert(0,"@")
    z.append("@")
    a.append(z)
    # a.append( [x for x in input()])
a.append(["@" for x in range(m + 2)])
for i in a:
    print(i)
for i in range(1,n):
    for j in range(1,m):
        print(a[i][j])
