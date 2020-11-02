n = int(input())
cub =[]
for i in range(1,n+1):
    if n%i == 0:
        cub.append(i)
print(cub)