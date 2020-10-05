txt = "sssssssss dddd wwwww ooooooooooo"
txt = txt.split(" ")
# txt = input().split(" ")
voc = {}
vv = []

for i in txt:
    vv.append(len(i))
vv = sorted(vv)
print(vv)
s = " ".join(map(str,vv))
for i in s:
    voc[i] = s.count(i)
for i in voc:
    if i != " ":
        print(i,voc[i],sep=": ")