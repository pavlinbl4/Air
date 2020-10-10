n = int(input())
m = n
a = []
for i in range(n):
    # a.append(list(map(int,input().split()))) создаем массив из чисел
    a.append(input().split())

for i in range(1,n):
    print()
    for j in range(1,m):
        print(a[i][j],end =" ")


