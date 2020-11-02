n, x = map(int,input().split())
a =[]
for i in range(1,n+1):
    a.append([z*i for z in range(1,n+1)])
count = 0
for i in range(n):
    for j in range(n):

        if a[i][j] == x:
            count += 1
print(count)
