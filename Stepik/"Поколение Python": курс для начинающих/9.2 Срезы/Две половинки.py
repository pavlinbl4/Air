st = "abcdefg"
if len(st)%2 == 0:
    x = int(len(st)/2)
else:
    x = int(len(st)/2) + 1
print(st[x:]+st[:x])

