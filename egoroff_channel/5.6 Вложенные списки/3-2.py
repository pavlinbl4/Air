n = int(input())
z=[]
for i in range(n):
    z.append([int(i) for i in input().split()])
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(z[j][i],end=' ')
    print()