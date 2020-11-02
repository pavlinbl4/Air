a, b = map(int,input().split())
count = 0
used = 0
while a > 0:
    a -= 1
    count += 1
    used += 1

    if used == b:
        a += 1
        used = 0
print(count)

