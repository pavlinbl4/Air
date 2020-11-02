
txt = input().split(" ")
voc = {}
vv = []
for i in txt:
    vv.append(len(i))
vv = sorted(vv)
voc = dict((x,vv.count(x)) for x in vv)
for i in voc:
    print(i,voc[i],sep=": ")