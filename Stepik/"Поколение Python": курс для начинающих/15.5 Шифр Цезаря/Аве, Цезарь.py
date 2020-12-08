txt = 'Day, mice. "Year" is a mistake!'
# print(txt.split())
txt = txt.split() # превращаю текст в список
for i in range(len(txt)): # обработка каждого слова в списке
    shift = 0
    print("txt[i] = ", txt[i])
    new = str()
    for x in txt[i]:
        if x.isalpha() == True:  # нахожу количество букв в слове
            print(x)
            shift += 1 # сдвиг равен количеству букв в слове

    for x in txt[i]:
        if x.isalpha() == True:
            if 97 <= ord(x) <= 122 - shift:
                new = new + chr(ord(x) + shift)
            else:
                new = new + chr(shift - 25 + ord(x))
            if 65 <= ord(x) <= 90 - shift:
                new = new + chr(ord(x) + shift)
            else:
                new = new + chr(shift - 25 + ord(x))
        else:
            new = new + x
    new = new +"*"
print(new)



