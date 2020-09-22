n = input()
rez =[]
n = n.lower()
a = 'A, O, Y, E, U, I'
a = a.lower()
for i in n:
    if i not in a:
        rez.append(i)
print("."+".".join(rez))

