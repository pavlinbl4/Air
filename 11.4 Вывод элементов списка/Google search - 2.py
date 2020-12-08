lst =[]
count = 0
for i in range(int(input())):
    lst.append(input())
ask=[]
for i in range(int(input())):
    ask.append(input())
for x in lst:
    count = 0
    # print("проверяю строку -", x)
    for y in range(len(ask)):
        # print("поисковый запрос -",ask[y].lower() )
        if ask[y].lower() in x.lower():
            count += 1
            # print("состояние счетчика -", count)
    if count == len(ask):
        # print("ВЫВОД - ", x, "@"*10)
        print(x)