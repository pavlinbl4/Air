n = int(input())
a = []
for x in range(n):
    m = set(input().split(", "))
    a.append(m)
for x in range(n):
    s = a[0].intersection(a[x])
if len(s) == 0:
    print("Фильм снять не удастся:(")
else:
    print(", ".join(s))
