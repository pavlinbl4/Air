n = int(input())
txt = input()
abc = "abcdefghijklmnopqrstuvwxyz"
# print(abc.index("k"))
# print(abc.index("w"))
for i in txt:
    x = abc.index(i)
    print(abc[x-n],end="")