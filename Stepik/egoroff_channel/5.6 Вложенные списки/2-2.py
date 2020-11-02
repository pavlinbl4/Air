n=int(input())
a=[input().split() for i in range(n)]
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[x][y], end=' ')
    print()
