voc = { "opel": 2345, "ford": 46536, "audi": 235}
lst = []
for i in voc:
    lst.append(i)
for i in sorted(lst):
    print(i,voc[i])