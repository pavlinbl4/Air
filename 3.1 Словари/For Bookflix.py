# создадим словарь библиотеки
book =  input().split(", ")
lybr = {}
for x in range(len(book)):
    book[x] = book[x].split(' (')
    book[x][1] = book[x][1][:-1]
    book[x][0] = book[x][0].split(' "')
    book[x][0][1] = book[x][0][1][:-1]
    book[x][0][1] = str(book[x][0][1])
    book[x][0].pop(0)
    # print(book[x][0])
    book[x][0] = "".join(book[x][0])
    # print(book[x])
    lybr.update([book[x]])
print(lybr)