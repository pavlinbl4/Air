n = int(input())
a = []
for i in range(n):
    x = set(input().split())
    y = set(input().split())
    a.append(len(x.intersection(y))/len(x))
print(a.index(max(a))+1)
