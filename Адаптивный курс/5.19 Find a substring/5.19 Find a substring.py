# x, y = input(), input()
x = "aaaa"
y = "aa"
def recur(x,y):
    if x.find(y) == -1:
        return x.find(y)
    return recur(x.find(y,x.find(y)+1),y)
print(recur(x,y))


