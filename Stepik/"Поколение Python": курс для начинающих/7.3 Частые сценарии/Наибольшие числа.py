n = int(input())
a = []
while n > 0 :
    n -= 1
    x = int(input())
    a.append(x)
a = sorted(a)

print(a[len(a)-1])
print(a[len(a)-2])