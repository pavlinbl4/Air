# n = int(input())
# st = str()
# for j in range(1,n+1):
#     st = st + " " + str(j)
#     print(st)


n = int(input())

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end = ' ')
    print()

