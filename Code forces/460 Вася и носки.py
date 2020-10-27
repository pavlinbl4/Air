n, m = map(int,input().split())
x = m
day = 0
while n > 0:
    day += 1
    n -= 1
    m -= 1
    if m == 0:
        n += 1
        m = x
print(day)