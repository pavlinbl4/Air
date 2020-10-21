p1, p2 = input(), input()
if len(p1) < 7:
    print("Short")
if len(p1) >= 7 and p1 == p2:
    print("OK")
elif len(p1) >= 7 and p1 != p2:
    print("Difference")
