n = int(input())
s = 0
for x in range(1,n+1):
    if n%x == 0:
        s += x
print(s)
