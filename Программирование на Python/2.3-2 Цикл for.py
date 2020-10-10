# a, b = (int(i) for i in input().split())
# print(a,b)

a,b = (int(input())  for x in range(2))
# print(a,b)
s = 0
k = 0
for x in range(a, b+1):
    if x%3 == 0:
        s+=x
        k+=1
print(s/k)