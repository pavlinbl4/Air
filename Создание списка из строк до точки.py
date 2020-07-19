""" 
подаем  последовательно строки со словами разделеными пробелами,
ввод происходит до точки, порлучаем списки вводимых строк
"""

lst = []
while True:
    w = input()
    if w == ".":
        # print(lst)
        # break
        continue
    else:
        lst.append(w.split())
        print(lst)


# """в виде функции"""
# def make_lst():
#     lst = []
#     while True:
#         w = input()
#         if w == ".":
#             return lst
#             #break
#         else:
#             lst.append(w.split())
# print(make_lst())