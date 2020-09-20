n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
s = []
for i in range(n):
    s.append(max(a[i]))
print(max(s))
print(s.index(max(s)),a[s.index(max(s))].index(max(s)))
