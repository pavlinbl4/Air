def library():
    book = input().split(", ")
    for x in range(len(book)):
        book[x] = book[x].split(' (')
        book[x][1] = book[x][1][:-1]
        book[x][0] = book[x][0].split(' ')
        book[x][0].pop(0)
        book[x][0] = " ".join(book[x][0])
        lybr.update([book[x]])
    return  lybr

def user_name(act):
    act = act.split(" (")  # тк пользватель в скобках избавляемся от скобок и узнаем имя пользователя
    act[1] = act[1][:-1]  # имя пользователя, который хочет почитать
    return act[1]

def book_shell(act,dict):
    act = act.split(' ')
    reader = act[0]
    act.pop(0)
    book_name = " ".join(act)
    dict.setdefault(reader, [])
    dict[reader].append(book_name)
    return dict

def test_genre():
    jan = ([lybr[x] for x in dict[user_name(act)]])  # узнаю жанры прочитанных книг
    # print("жанры прочитанных книг -",jan)
    global sort_jan
    sort_jan = {}  # словарь где будет любимые жанры

    for x in range(len(jan)):
        ss = jan.count(jan[x])
        sort_jan[jan[x]] = ss

    # print("словарь любимых жанров -", sort_jan) # тут все данные выводятся
    return sort_jan


def test_name():
    if dict.get(user_name(act)) == None:
        print("Список пуст - пользователь не прочел ни одной книги")
    else:
        test_genre()
        # print("словарь любимых жанров -", sort_jan)  # тут все данные выводятся
        return sort_jan



def _genre():
    global oth
    oth = []  # все книги этого жанра

    if sort_jan[max(sort_jan, key=sort_jan.get)] == 1:  # счетчик у любимого жанра равен 1
        for x in sort_jan:
            if sort_jan[x] == 1:
                for nnn in [x for x in sort_jan if sort_jan[x] == 1]:
                    for x in lybr:
                        if lybr[x] == nnn:
                            oth.append(x)
    elif sort_jan[max(sort_jan, key=sort_jan.get)] == 0:
        print("Список пуст")
    else:
        for x in sort_jan:
            if sort_jan[x] > 1:
                for nnn in [x for x in sort_jan if sort_jan[x] > 1]:
                    for x in lybr:
                        if lybr[x] == nnn:
                            oth.append(x)
    return oth

def recomendation():

    notread = []  # список непрочитанных книг по заданному жанру
    for dd in range(len(oth)):
        if oth[dd] not in dict[user_name(act)]:
            if oth[dd] not in notread:
                notread.append(oth[dd])
        # print("все книги данного жанра -", oth)
    if len(notread) == 0:
        print("Список пуст")
    else:
        print(', '.join(notread))


# lybr = {}
# library() # функция создающая словарь книг в библиотеке lybr
lybr = {'"Собачье сердце"': 'сатира', '"Властелин колец"': 'фэнтези', '"Затерянный мир"': 'научная фантастика', '"Десять негритят"': 'детектив', '"Сияние"': 'ужасы', '"Отравленный пояс"': 'научная фантастика', '"Зов Ктулху"': 'ужасы', '"Изучаем Python"': 'учебная литература', '"C++ за 21 день"': 'ужасы', '"Хоббит"': 'фэнтези', '"Долина ужаса"': 'детектив', '"Оно"': 'ужасы', '"Убийство в доме викария"': 'детектив', '"Противостояние"': 'ужасы', '"Марсианин"': 'научная фантастика'}

dict = {} # словарь пользователей и прочтенных им книг
while True:
    act = input() # ввод запроса
    if act == ".": # если точка, то программа останавливается
        break
    else: # рассмотрим варианты запросов
        if "Посоветуй" in act:  # если в запросе есть слово "Посоветуй", то определяем имя пользователя
            user_name(act) # пользователь, просщий совета
            test_name()  # проверяю читал ли пользователь книги, если да то получаю словарь люимых жанров  sort_jan
            # print("словарь любимых жанров -", test_name())
            _genre() # функция определяющая всех книг даного жанра name 'sort_jan' is not defined не могу разобраться почему
            # print("словарь любимых жанров -", sort_jan)
            # recomendation() #рекомендованные к прочтению книги

        else:
            book_shell(act, dict) # прочитанные пользователем книги
# print("словарь любимых жанров -", sort_jan)
print(dict)
print(lybr)





