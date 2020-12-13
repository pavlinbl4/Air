rez = {}
with open("/Volumes/big4photo/Downloads/dataset_3380_5.txt",'r') as sheet:
    for line in sheet:
        one_line = line.strip().split("\t")
        rez[one_line[0]] = rez.get(one_line[0],[])
        rez[one_line[0]].append(one_line[2])
# print(rez)
for i in range(1,12):
    # print(i,"-----",rez.get(str(i)))
    if rez.get(str(i)) != None:
        print(i,'&&&',rez[str(i)])
    else:
        print(i,"-")

