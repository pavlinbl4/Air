n = int(input())
level = 1
count = 0
next = 0
while n >= next :

    count = level + count
    level = level + 1
    n -= count
    next = level + count
print(level -1)

    # print("level -", level-1," ","count -", count," ", "next -",next," ", n)


