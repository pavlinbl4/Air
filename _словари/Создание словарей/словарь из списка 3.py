"""
есть список со строками - создать словарь где ключ четное
значение списка, а
"""
spisok = ["fox", 33, "book", 77, "table", 88, "sky", 100]
voc = {spisok[x - 1]: spisok[x] for x in range(1, len(spisok), 2)}
print(voc)
