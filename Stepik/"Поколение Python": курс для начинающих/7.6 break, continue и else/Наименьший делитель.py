n = int(input())
for i in range(2,n+1):
    # print("i =", i , "  ","n % i =",n % i)
    if n % i == 0:
        break
print(i)
