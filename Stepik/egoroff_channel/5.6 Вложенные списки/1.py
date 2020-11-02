# a = []
# sum = []
# n = int(input())
# m = n
# for i in range(n):
#     b = []
#     for i in range(m):
#         b.append(input())
#
#     a.append(b)
# for i in a:
#     print(i)

a = []
ss = []
# n = int(input())
n = 5
for i in range(n):

    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i == j:
            ss.append(a[i][j])
print(sum(ss))