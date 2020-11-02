n = list(input().split("#"))
n.pop(0)
n = int(n[0])

lst = 0
for i in range(n):
    x = input()
    if "#" not in x:
        print(x)
    else:
        lst = x.split("#")
        print(lst[0].rstrip())

