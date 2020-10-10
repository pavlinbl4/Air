n = int(input())
big1 = 0
big2 = 0
for i in range(n+1):
    x = int(input())
    if x > big1:
        big1 = i
        if big2 < x < big1:
            big2 = i
print(big1)
print(big2)