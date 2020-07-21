
# book = input() список книг сервиса
book = 'Булгаков "Собачье сердце" (сатира), Толкин "Властелин колец" (фэнтези), Дойл "Затерянный мир" (научная фантастика), Кристи "Десять негритят" (детектив), Кинг "Сияние" (ужасы), Дойл "Отравленный пояс" (научная фантастика), Лавкрафт "Зов Ктулху" (ужасы), Лутц "Изучаем Python" (учебная литература), Рао "C++ за 21 день" (ужасы), Толкин "Хоббит" (фэнтези), Дойл "Долина ужаса" (детектив), Кинг "Оно" (ужасы), Кристи "Убийство в доме викария" (детектив), Кинг "Противостояние" (ужасы), Вейер "Марсианин" (научная фантастика)'
# act = input() ввод информации о прочтении или запрос совета
# act = "Dontsova "Десять негритят""
# act = "Посоветуй мне книгу (Maria)"

# создадим словарь библиотеки  где названи е книги и жанр
# book =  input().split(", ")
# lybr = {}
# for x in range(len(book)):
#     book[x] = book[x].split(' (')
#     book[x][1] = book[x][1][:-1]
#     book[x][0] = book[x][0].split(' "')
#     book[x][0][1] = book[x][0][1][:-1]
#     book[x][0][1] = str(book[x][0][1])
#     book[x][0].pop(0)
#     book[x][0] = "".join(book[x][0])
#     lybr.update([book[x]])
lybr = {'Собачье сердце': 'сатира', 'Властелин колец': 'фэнтези', 'Затерянный мир': 'научная фантастика', 'Десять негритят': 'детектив', 'Сияние': 'ужасы', 'Отравленный пояс': 'научная фантастика', 'Зов Ктулху': 'ужасы', 'Изучаем Python': 'учебная литература', 'C++ за 21 день': 'ужасы', 'Хоббит': 'фэнтези', 'Долина ужаса': 'детектив', 'Оно': 'ужасы', 'Убийство в доме викария': 'детектив', 'Противостояние': 'ужасы', 'Марсианин': 'научная фантастика'}



# начнем с ввода запросов
dict = {} # словарь пользователей и прочтенных им книг
# dict = {'Dontsova': ['Десять негритят', 'Долина ужаса'], 'Jerry': ['Зов Ктулху', 'Противостояние', 'Затерянный мир', 'Отравленный пояс'], 'Maria': ['Хоббит', 'Властелин колец']}
while True:
    act = input()
    if act == ".":
        break
    else:
        if "Посоветуй" in act:
            act = act.split(" (")
            act[1] = act[1][:-1] # имя пользователя, который хочет почитать
            print("пользователь, который просит совета - ",act[1])  # пользователь, который просит совета
            print("прочитанные книги -", dict[act[1]]) # уже прочитанные книги
            jan = ([lybr[x] for x in dict[act[1]]]) # узнаю жанры прочитанных книг
            print("жанры прочитанных книг -",jan)
# надо узнать какой жанр повторяется чаще всего
            sort_jan = {}  # словарь где будет любимые жанры
            for x in range(len(jan)):
                ss = jan.count(jan[x])
                sort_jan[jan[x]] = ss
            # print("любимые жанры - ",sort_jan)
            # fav_jan = max(sort_jan, key=sort_jan.get) # любимый жанр, ( это искать не нужно , надо использовать все жанры
            # print("жанр по которому ищем вариант -", fav_jan)
            # нужно получить все книги этого жанра кроме прочитанных
            oth = [] # все книги этого жанра
            notread = []  # список непрочитанных книг по заданному жанру
            # for nnn in list(sort_jan): #преобразование ключей к списку оказалось неправильной идеей, ноужны жанры , которые повторяются чаще
            for nnn in [ x for x  in sort_jan if sort_jan[x] >  1 ]:# тоже не вариант, отбрасываются жанры с цифрой 1
                for x in lybr:
                     if lybr[x] == nnn:

                        oth.append(x)
            # # print("все книги данного жанар -",oth)
                for dd in range(len(oth)):
                    if oth[dd] not in dict[act[1]]:
                        if oth[dd] not in notread:
                            notread.append(oth[dd])
            print("непрочитанные(рекомендуемые) книги данного жанра -",notread)
            print()
            # break
        else:
            act = act.split(' "')
            act[1] = act[1][:-1]
            dict.setdefault(act[0], [])
            dict[act[0]].append(act[1])



