n, m = map(int,input().split())
a = []

for i in range(n):
    a.append([x for x in input()])

for i in range(n):
    a[i].insert(0,"@")
    a[i].append("@")
for j in range(m):


for i in a:
    print(i)
