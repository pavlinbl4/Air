:n = int(input())
y = int(len(str(n))/2)
if len(str(n))%2 != 0:
    print("вы ввели некорректное число")
else:
    dl = n//10**y
    dr = n%10**y
    sl = 0
    sr = 0
    for x in range(y):
        sl = sl + dl%10
        sr = sr + dr%10
        dr = dr//10
        dl = dl//10
    if sl == sr:
        print("YES")
    else:
        print("NO")


