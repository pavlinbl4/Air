a, b = map(int, input().split())
x = abs(a*b)
while b != 0:
    a, b = b, a % b
nod = a
print(int(x/nod))