# n  = int(input())
n = 6743
sum1 = 0
while n > 9:
    while n > 0:
        sum1 = sum1 + n%10
        n = n//10
    n = sum1
    print(n)
print("itog =", n)