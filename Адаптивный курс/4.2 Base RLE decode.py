d = "13ab44c2CaB"
# d = input()
l = [x for x in d]
rez = []
for x in range(len(l)):
    if l[x].isdigit() == True:
        rez.append((int(l[x])-1)*(l[x+1]))
    else:
        rez.append(l[x])
print("".join(rez))

