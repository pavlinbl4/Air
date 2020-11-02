d = []
n = set(input().split())
m = set(input().split())
for i in (n.difference(m)):
    d.append(i)
print(*sorted(d))


