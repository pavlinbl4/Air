dig =[ 2, 3,4 ]
s = []
z = 1
for x in reversed(range(len(dig))):
    s.append(dig[x] * z)
    z = z * 10
print(sum(s))