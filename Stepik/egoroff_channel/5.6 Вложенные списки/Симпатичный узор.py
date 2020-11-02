n = int(input())
# n = 4
a =[]
for i in range(n):
    a.append([x for x in input()])
# for i in a:
#     print(i)
# print("*"*50)
s = 0
for i in range(n-1):
    for j in range(n-1):
        if a[i][j] == a[i+1][j] and a[i][j+1] == a[i+1][j+1]:
            s += 1
            break

if s == 0:
    print("YES")
else:
    print("NO")
