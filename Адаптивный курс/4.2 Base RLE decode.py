d = "13ab44c2CaB"
# d = input()
l = [x for x in d ]
print(l)
rez = []
for x in reversed(range(len(l))):
    if l[x].isdigit() == True and l[x-1].isdigit() != True:
        rez.append((int(l[x])-1)*(l[x-1]))
    else:
        rez.append(l[x])
print("".join(rez))

