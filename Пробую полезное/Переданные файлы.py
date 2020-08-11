"""1.на вход подается скопированная информация ищ истории съемки
вместе со строкой со словом ПЕРЕДАЧА на выходе получаем словарь
с именами опубликованных файлов
2.на вход подаю таблицу переданных файлов, по окончании ставлю точку,
получаю словарь новое- старое имя файла"""
upload = {} # все переданные файлы
while True:
    n = input()
    if n == '.':
        break
    else:
        line = []
        s = n.find("JPG")
        s1= n.rfind("JPG")
        line.append(n[s + 4:s1 - 3])
        line.append(n[:s-1])
        upload.update([line])
# print(upload)
# published ={}
while True:
    n = input()
    if "передача" in n :
        break
    else:
        s=n.find("KSP")
        s1=n.find("_1")
        used_file=(n[s:s1])
        print(used_file, " -", upload[used_file])

