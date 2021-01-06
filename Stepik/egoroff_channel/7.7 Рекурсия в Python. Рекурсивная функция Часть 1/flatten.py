def flatten(s):
    if len(s) == 0:
        return []
    if isinstance(s[0],list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])

print(flatten([[[[9]]], [1, 2], [[8]]]))
