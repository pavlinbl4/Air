# print(*[x for x in input() if x.isdigit()],sep='')
[print(x,end='') for x in input() if x.isdigit()]