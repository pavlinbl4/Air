st = "malina"
def ss(st):
    if len(st) == 1 or len(st) == 2:
        return st
    return st[0] + "(" + ss(st[1:-1]) + ")" + st[-1]

print(ss(st))

