def mp(dig):
    s = []
    z = 1
    for x in reversed(range(len(dig))):
        s.append(dig[x] * z)
        z = z * 10
    return sum(s)
d = input()
l = [x for x in d]
rez = []
dig = []
for x in range(len(l)):
    if l[x].isdigit() == True:
        dig.append(int(l[x]))
    else:
        if len(dig) == 0:
            rez.append(l[x])
        else:
            rez.append(mp(dig)*l[x])
            dig.clear()
print("".join(rez))

