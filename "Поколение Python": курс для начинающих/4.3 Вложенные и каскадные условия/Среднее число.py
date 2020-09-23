a, b, c = int(input()),int(input()),int(input())
if a < b < c  or c < b < a:
    print(b)
elif b < c < a  or a < c < b:
    print(c)
else:
    print(a)