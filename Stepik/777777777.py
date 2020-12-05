n = int(input())
lst = []
for x in range(1,n+1):
    if len(lst) < n:
        lst = lst + [x]*x
print(*lst[:n])

