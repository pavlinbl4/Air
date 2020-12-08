n = int(input())
lst = [int(i) for i in  input().split()]
# print(lst)
count = [0] * 201
for i in lst:
    count[i + 100] += 1
# print(count)
for i in range(201):
    if count[i] > 0:
        print( (str(i-100) +' ') * count[i],end="")
