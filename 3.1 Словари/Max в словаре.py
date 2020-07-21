"""
словарь, где ключ слово, а значение цифра, нужно найти ключ с максимально большой цифрой
"""
sort_jan = {'детектив': 2, 'фантастика': 3, 'ужасы': 1}
print(max(sort_jan,key=sort_jan.get))
print()

"""
рассмотреть два варианта, где значения больше 2 и только 1
"""
print("рассмотреть два варианта, где значения больше 2 и только 1".upper())
print(sort_jan[max(sort_jan,key=sort_jan.get)])
if sort_jan(max(sort_jan,key=sort_jan.get)) >1:













"""
другой вариант задачи, нужны ключи тех значений, которые больше 1
"""
# print(len(sort_jan))
print("следующий вариант")
print()
for x in sort_jan:
    if sort_jan[x] > 1:
        print("жанр -",x)
        print(sort_jan[x])



    if sort_jan[x] >1:
        print("прочитанно много книг - ",[x for x in sort_jan if sort_jan[x] > 1])
    else:
        print("прочитанна  одна книга - ",[x for x in sort_jan])



