"""
есть список со строками - создать словарь где ключ меняется от еденицы , а строки из списка это значения
"""
spisok = ["fox","book","table","sky"]
voc = { x : spisok[x-1] for  x in range(1,len(spisok)+1)}
print(voc) # {1: 'fox', 2: 'book', 3: 'table', 4: 'sky'}