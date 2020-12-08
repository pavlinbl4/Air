n = int(input())
count = [0]*10
while n > 0:
    count[n%10] += 1
    n = n//10
# print(count)
for i in range(10):
    if count[i]> 0:
        print(i, count[i])