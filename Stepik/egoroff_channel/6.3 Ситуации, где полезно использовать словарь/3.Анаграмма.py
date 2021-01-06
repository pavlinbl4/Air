# s1 = "abracadabra"
# s2 = "cadabraabrg"
s1 = input()
s2 = input()
d1 = {}
d2 = {}
if len(s1) == len(s2):
    for i in range(len(s1)):
        d1[s1[i]] = d1.get(s1[i],0) + 1
        d2[s2[i]] = d2.get(s2[i], 0) + 1
    # print(d1)
    # print(d2)
    count = 0
    for i in d1:
        if d1[i] != d2[i]:
            count += 1
    if count == 0:
        print("YES")
    else:
        print("NO")





else:
    print("NO")