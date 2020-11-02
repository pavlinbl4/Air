n = int(input())
cub =[]
ss = []
for i in range(n):
    cub.append(int(input()))

for i in range(n-1):
    ss.append(cub[i] + cub[i+1])
print(ss)