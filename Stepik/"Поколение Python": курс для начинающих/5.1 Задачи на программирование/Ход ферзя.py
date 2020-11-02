a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# a1, b1, a2, b2 = 4, 4, 1, 1
if abs(a1-a2) == abs(b1-b2) or a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")