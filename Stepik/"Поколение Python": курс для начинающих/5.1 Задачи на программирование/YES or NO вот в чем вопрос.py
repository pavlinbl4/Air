x = int(input())
if x % 2 != 0 or x % 2 == 0 and 6 <= x <= 20:
    print("YES")
elif x % 2 == 0 and 2 <= x <= 5 or x % 2 == 0 and x > 20:
    print("NO")
