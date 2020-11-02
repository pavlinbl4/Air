n = int(input())
count = 0
while n >= 0 and n < 6 :
    if n == 5:
        count += 1
    n = int(input())
print(count)