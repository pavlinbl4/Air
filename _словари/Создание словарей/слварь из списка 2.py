"""
есть список со строками - создать словарь где ключ меняется от еденицы , а строки из списка это значения
"""
spisok = ["fox","book","table","sky"]
voc = {spisok[x-1]:x for  x in range(1,len(spisok)+1)}
print(voc) # {'fox': 1, 'book': 2, 'table': 3, 'sky': 4}