# новый оптимизатор ключевых слов
from datetime import date
txt = open('keywords in work.txt', 'a')
date = str(date.today())


keywords = input()
keywords = keywords.replace("?", "й") # исправляет иногда возникающую ошибку при которой  "й" отображается как "?"
keywords = keywords.replace(",", "*")
keywords = keywords.replace("|", "*")
keywords = keywords.replace(";", "*")
keywords = keywords.replace("  ", "*")
keywords = keywords.replace(" ", "*")
keywords = keywords.replace(".", "*")
b = set(keywords.split("*"))
b = sorted(b)
print(b)
print(type(b[0]))
keywords = str
for i in b:
    if len(i) !=0:
        c = keywords+i
        print("keywords  - ",c)



print(", ".join(b))
# txt.write(date+'\n')
# txt.write(str(b)+'\n')


