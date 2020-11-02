st = input()
def palindrom(st):
    if len(st) == 1 or len(st) == 0:
        print("YES")
    elif st[0] == st[-1]:
        return palindrom(st[1:-1])
    else :
        print("NO")

palindrom(st)
