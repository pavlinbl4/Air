a = int(input())
b = int(input())
c = int(input())
# dd = [a, b, c, b, a, b, c, b] 2a 3b 2c
# один цикл горения прожекторов 8 сек , после цикла "a" "c" уменьшаются на 2, "b" уменьшается на 4
min_light = min([a//2, b//4, c//2])


count = 8 * min_light
a = a - 2 * (min_light)
b = b - 4 * (min_light)
c = c - 2 * (min_light)


while True:
    if a >= 1:
        a -= 1
        count += 1
    else:
        break
    if b >= 1:
        b -= 1
        count += 1
    else:
        break
    if c >= 1:
        c -= 1
        count += 1
    else:
        break
    if b >= 1:
        b -= 1
        count += 1
    else:
        break
    if a >= 1:
        a -= 1
        count += 1
    else:
        break
    if b >= 1:
        b -= 1
        count += 1
    else:
        break
    if c >= 1:
        c -= 1
        count += 1
    else:
        break
    if b >= 1:
        b -= 1
        count += 1
    else:
        break
print(count)
