# создадим словарь библиотеки где книги в кавычках
book = input().split(", ")
lybr = {}
for x in range(len(book)):
    book[x] = book[x].split(' (')
    book[x][1] = book[x][1][:-1]
    book[x][0] = book[x][0].split(' ')
    book[x][0].pop(0)
    book[x][0] = " ".join(book[x][0])
    lybr.update([book[x]])
# lybr = {'"Собачье сердце"': 'сатира', '"Властелин колец"': 'фэнтези', '"Затерянный мир"': 'научная фантастика', '"Десять негритят"': 'детектив', '"Сияние"': 'ужасы', '"Отравленный пояс"': 'научная фантастика', '"Зов Ктулху"': 'ужасы', '"Изучаем Python"': 'учебная литература', '"C++ за 21 день"': 'ужасы', '"Хоббит"': 'фэнтези', '"Долина ужаса"': 'детектив', '"Оно"': 'ужасы', '"Убийство в доме викария"': 'детектив', '"Противостояние"': 'ужасы', '"Марсианин"': 'научная фантастика'}

# начнем с ввода запросов
dict = {} # словарь пользователей и прочтенных им книг
while True:
    act = input() # ввод запроса
    if act == ".": # если точка, то программа останавливается
        break
    else: # расмотрим варианты запросов
        if "Посоветуй" in act: # если в запросе есть слово "Посоветуй", то определяем имя пользователя
            act = act.split(" (") # тк пользватель в скобках избавляемся от скобок и узнаем имя пользователя
            act[1] = act[1][:-1] # имя пользователя, который хочет почитать
            if dict.get(act[1]) == None:
                print("Список пуст")#- пользователь не прочел ни одной книги")
            else:
            # print("пользователь, который просит совета - ",act[1])
            # print("прочитанные книги -", dict[act[1]])
                if len(dict) == 0:
                    print("Список пуст")
                else:
                    jan = ([lybr[x] for x in dict[act[1]]]) # узнаю жанры прочитанных книг
                    # print("жанры прочитанных книг -",jan)
                    sort_jan = {}  # словарь где будет любимые жанры
                    for x in range(len(jan)):
                        ss = jan.count(jan[x])
                        sort_jan[jan[x]] = ss
                    # print("словарь любимых жанров -",sort_jan )

                    oth = [] # все книги этого жанра
                    notread = []  # список непрочитанных книг по заданному жанру
                    if sort_jan[max(sort_jan, key=sort_jan.get)] == 1: # счетчик у любимого жанра равен 1
                        for x in sort_jan:
                            if sort_jan[x] == 1:
                                for nnn in [ x for x  in sort_jan if sort_jan[x] ==  1 ]:
                                    for x in lybr:
                                        if lybr[x] == nnn:
                                            oth.append(x)
                    elif  sort_jan[max(sort_jan, key=sort_jan.get)] == 0:
                        print("Список пуст")
                    else:
                        for x in sort_jan:
                            if sort_jan[x] > 1:
                                for nnn in [ x for x  in sort_jan if sort_jan[x] >  1 ]:
                                    for x in lybr:
                                        if lybr[x] == nnn:
                                            oth.append(x)


                    for dd in range(len(oth)):
                            if oth[dd] not in dict[act[1]]:
                                if oth[dd] not in notread:
                                    notread.append(oth[dd])
                    # print("все книги данного жанра -", oth)
                    if len(notread) == 0:
                        print("Список пуст")
                    else:
                        print(', '.join(notread))
        else: # создаем словарь прочетнных пользователем книг
            act = act.split(' ')
            reader = act[0]
            act.pop(0)
            book_name = " ".join(act)
            dict.setdefault(reader, [])
            dict[reader].append(book_name)




