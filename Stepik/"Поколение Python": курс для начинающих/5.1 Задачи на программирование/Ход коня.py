a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# a1, b1, a2, b2 = 4, 3, 4, 5
if abs(a1-a2) == 2 and abs(b1-b2) == 1 or abs(a1-a2) == 1 and abs(b1-b2) == 2:
    print("YES")
else:
    print("NO")