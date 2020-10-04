txt = "sssssssssw dddd"
txt = txt.split(" ")
# txt = input().split(" ")
voc = {}
vv = []
for i in txt:
    vv.append(len(i))
vv = sorted(vv)
# print(vv)
s = ", ".join(vv)
# print(s)
for i in s:
    print(i)
    voc[i] = s.count(i)
print(voc)
for i in voc:
    if i != " ":
        print(i,voc[i],sep=": ")