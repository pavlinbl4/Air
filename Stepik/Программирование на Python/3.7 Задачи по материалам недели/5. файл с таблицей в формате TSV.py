rez = {}
with open("/Users/evgeniy/Downloads/dataset_3380_5-2.txt",'r') as sheet:
    for line in sheet:
        one_line = line.strip().split("\t")
        rez[one_line[0]] = rez.get(one_line[0],[])
        rez[one_line[0]].append(one_line[2])

itog = open("/Users/evgeniy/Downloads/itog.txt",'w')

for i in range(1,12):
    if rez.get(str(i)) != None:
        rez[str(i)] = list(map(int,rez[str(i)]))
        print(i,sum(rez[str(i)])/len(rez[str(i)]))
        x = str(i)+" "+str(sum(rez[str(i)])/len(rez[str(i)]))
        itog.write(x +'\n')
    else:
        print(i,"-"+"\n")
        itog.write(str(i) +" -"+ '\n')

