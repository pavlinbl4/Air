n = int(input())
for i in range(1,n+1):
    count = 0
    print(i,end="")
    for delitel in range(1,i+1):
        if i % delitel == 0:
            count += 1
    print("+"*count,end='')
    print()