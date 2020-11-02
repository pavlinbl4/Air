lst =[]
for i in range(int(input())):
    x = input()
    if x not in lst:
        lst.append(x)
print(*lst,sep='\n')