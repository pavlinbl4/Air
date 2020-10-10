a,b,c,d = (int(input())  for x in range(4))
# a,b,c,d = 7, 10, 5, 7
for z in range(c,d+1):
    print("",end="\t")

    print(z,end="")
    # print()

print()
for i in range(a,b+1):
    print(i,end="\t")

    for j in range(c,d+1):
        print(i * j, end="\t")
    print()


