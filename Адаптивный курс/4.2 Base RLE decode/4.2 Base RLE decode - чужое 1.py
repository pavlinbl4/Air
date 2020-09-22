# 44d5W7sABC
WW = "44d5W7sABC"


s = ''.join(char + ' ' if char.isalpha() else char for char in WW).split()
print(s)
print([int(i[:-1]) * i[-1] if len(i) > 1 else i for i in s])
print(''.join(int(i[:-1]) * i[-1] if len(i) > 1 else i for i in s))