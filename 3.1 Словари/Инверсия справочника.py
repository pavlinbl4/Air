"""Вам поручено реализовать справочник, который умеет искать информацию в обе стороны, то есть по запросу о стране
справочник должен выводить ее столицу, а по запросу о столице – страну.
Программа принимает на вход пары "страна-столица" через двоеточие, пары вводятся до символа точки.
Затем следуют строки до символа точки, состоящие из одного географического объекта:
справочник должен ответить на эти запросы.
Если запрашиваемого объекта нет в справочнике, необходимо вывести "Нет данных"."""
# def read(gg):
#     gg_r = {v: k for k, v in gg.items()}
#     while True:
#         w = input()
#         if w == ".":
#             break
#         else:
#             if w in gg  == True:
#                 print(gg[w])
#             elif w in gg_r == True:
#                 print(gg_r(w))
#             else:
#                 print("Нет данных")





gg = {}
while True:
    s = input()
    if s == ".":
        # read(gg)
        gg_r = {v: k for k, v in gg.items()}
        while True:
            w = input()
            if w == ".":
                break
            else:
                if gg.get(w) != None:
                    print(gg[w])
                elif gg_r.get(w) != None:
                    print(gg_r[w])
                else:
                    print("Нет данных")

        break
    else:
        t = s.split(": ")
        # print(t)
        gg[t[0]] = t[1]
