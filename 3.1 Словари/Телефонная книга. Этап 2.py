"""Коля понял, что у многих из его знакомых есть несколько телефонных номеров и нельзя хранить только один из них.
Он попросил доработать Вашу программу так, чтобы можно было добавлять к существующему контакту новый номер
или даже несколько номеров, которые передаются через запятую. По запросу телефонного номера должен выводиться
весь список номеров в порядке добавления, номера должны разделяться запятой.
Если у контакта нет телефонных номеров, должна выводиться строка "Не найдено"."""


phonebook ={}
while True:
    s = input()
    if s == ".":
        break
    else:
        text = s.replace(",","").split()
        if len(text) >= 2 and phonebook.get(text[0]) == None:
            phonebook[text[0]] = [text[x] for x in range(1,len(text))]
        elif len(text) >= 2 and phonebook.get(text[0]) != None:
            add = (", ".join(map(str,[text[x] for x in range(1, len(text))])))
            phonebook[text[0]].append( add )
        else:
            if phonebook.get(text[0]) == None:
                print("Не найдено")
            else:
                print(*phonebook[text[0]],sep=', ')

