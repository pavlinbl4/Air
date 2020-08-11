"""на вход подается скопированная информация ищ истории съемки
вместе со строкой со словом ПЕРЕДАЧА на выходе получаем словарь
с именами опубликованных файлов"""
upload = {} # все переданные файлы
published ={}
while True:
    n = input()
    if "передача" in n :
        line = []
        s = n.find("JPG")
        if s != -1:
            s1 = n.rfind("JPG")
            line.append(n[s + 4:s1 - 3])
            line.append(n[:s - 1])
            upload.update([line])
            

        break
    else:
        s=n.rfind("Добавлен: KSP")
        if s != -1:
            used_file=(n[s+20:s+30])
            published.setdefault(n[s+10:s+26])
print()
print(published)