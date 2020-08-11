"""
лучший вариант, на вход подачать копию развернутой страницы истории съемки
"""
upload = {}
published = []
while True:
    n = input()
    if n == ".":
        print(published)
        print(upload)
        for x in range(len(published)):
            print(upload[published[x]]," - ",published[x] )
        break
    elif n.find("Добавлен:") != -1:
            published.append(n[n.find("Добавлен:")+10:n.find("Добавлен:")+26])
    elif n.find("JPG") != -1:
        line = []
        line.append(n[n.rfind("JPG") - 19:n.rfind("JPG") - 3])
        line.append(n[:n.find("JPG")-1])
        upload.update([line])




