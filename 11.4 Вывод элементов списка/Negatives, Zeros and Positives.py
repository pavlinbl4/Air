neg =[]
zer = []
plus = []
for i in range(int(input())):
    x = int(input())
    if x < 0:
        neg.append(x)
    elif x == 0:
        zer.append(x)
    elif x > 0:
        plus.append(x)
print(*(neg+zer+plus),sep='\n')