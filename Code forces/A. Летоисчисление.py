a, n = int(input()),int(input())
if a * n > 0:
    print(a + n)
else:
    if a > 0 and a + n < 1:
        print(a + n - 1)
    elif a < 0 and a + n > -1:
        print( a + n + 1)
    else:
        print(a + n)