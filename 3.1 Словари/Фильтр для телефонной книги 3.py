def standart():
    if phones[x] != 0:
        dd = [x for x in phones[x]]  # преобразую стоку в список
        if dd[0] == '8':  # если номер начинается с восьмерки заменяю на +7
            dd.pop(0)
            dd.insert(0, "7")
            dd.insert(0, "+")
        dd.insert(2, " ")  # форматирую номер по стандарту, добавляя скобки и тире
        dd.insert(3, "(")
        dd.insert(7, ")")
        dd.insert(8, " ")
        dd.insert(12, "-")
        dd.insert(15, "-")
        phones[x] = "".join(dd)  # обратно преобразую список к строке
        return phones[x]

def optimize():
    phones[x] = phones[x].replace(" ","")
    phones[x] = phones[x].replace("-","")
    phones[x] = phones[x].replace("(","")
    phones[x] = phones[x].replace(")","")
    return phones[x]

def clear(phones):
    for x in range(phones.count(0)):
        phones.remove(0)
    return phones

def chek(name,phones,phonebook):
    if name in phonebook:
        phonebook[name].append(phones)
    else:
        phonebook = {name: phones}
        return phonebook


phonebook ={}
while True:
    s = input()
    if s == ".":
        break
    else:
        x = s.find(" ") # нахожу первый пробел, который отделяет имя
        if x == -1: # в данном случае идет запрос номера
            name = s
            if name in phonebook:
                if phonebook[name] == []:
                    print("Не найдено")
                else:
                    print(*phonebook[name],sep=', ')
            else:
                print("Не найдено")
        else:# добавляем информацию в телефонную книгу
            name  = s[:x] # берем срез где имя абонента
            numb = s[x+1:] # берем срез где номера
            phones = numb.split(",") # создаю список телефонов
            for x in range(len(phones)): # удаляю пробелы и тд в номерах
                optimize()
                # if (phones[x][0] == "+" and phones[x][1] != "7") or (len(phones[x]) == 12 and phones[x][0] != "+") or (len(phones[x]) == 11 and phones[x][0] != "8" or len(phones[x]) < 11 or len(phones[x]) > 12):
                if (phones[x][0] == "+" and phones[x][1] != "7")  or (
                        len(phones[x]) == 11 and phones[x][0] != "8" or len(phones[x]) < 11 or len(phones[x]) > 12):
                    phones[x] = 0 # заменяю на ноль некорректный номер
                else:
                    standart()
            clear(phones)#  функция удаляющая нули из списка phones
            if name in phonebook:
                add = (", ".join(map(str,[phones[x] for x in range(len(phones))])))
                phonebook[name].append(add)
            else:
                phonebook[name] = phones













