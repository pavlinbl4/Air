st = input()
flag = 0
for x in st:
    if x != "(" and x != ")" and x != "[" and x != "]" and x != "{" and x != "}":
        flag += 1
        break
if flag > 0:
    print("NO")
else:
    # print("в строке только скобки продолжаем проверку")
    lst = []
    for i in st:
        lst.append(i)
    # print("start ",lst)
    l = len(lst)
    x = 0
    while l > 0 and x < l:
        if lst[x] == "[" and lst[x + 1] == "]" or lst[x] == "(" and lst[x + 1] == ")" or  lst[x] == "{" and lst[x + 1] == "}":
            lst.pop(x)
            lst.pop(x)
            l -= 2
            x = 0
            continue
        x += 1
    if len(lst) == 0:
        print('YES')
    else:
        print("NO")



# print("конец проверки")



