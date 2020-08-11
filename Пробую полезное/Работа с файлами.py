# запись текста в файл

n = open('text.txt','w')
while True:
    m = input()
    if m ==".":
        break
    else:

        n.write(m+'\n')