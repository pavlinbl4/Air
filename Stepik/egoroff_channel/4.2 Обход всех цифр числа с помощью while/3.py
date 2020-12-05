n = int(input())
count = 0
while n > 0:
    if n%10 == 7:
        count += 1
    n = n//10
print(count)
