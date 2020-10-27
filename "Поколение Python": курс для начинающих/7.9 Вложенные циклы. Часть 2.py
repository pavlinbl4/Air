n = int(input())
x = 0
for i in range(1,n+1):
    print()
    for j in range(i,i + i):
        x += 1
        print(x,end=" ")