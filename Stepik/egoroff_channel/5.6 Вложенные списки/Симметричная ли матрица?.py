n = int(input())
a = []
s = 0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        # print(a[i][j],"(", i,j,")" "-", a[j][i],"(", j,i,")")
        if a[i][j] == a[j][i]:

            s = s + s
        else:
            # print("not", a[i][j], "-", a[j][i])
            s = -1
if s == 0:
    print("YES")
else:
    print("NO")


