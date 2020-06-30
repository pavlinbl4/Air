"""
Стремясь стать программистом, важно не только постоянно учиться,
но и понимать язык, на котором говорят Ваши коллеги.
Чтобы систематизировать знания, Вы решили написать программу,
которая составляет маленький словарь из сленговых выражений.
Программа принимает на вход строки до символа точки, состоящие из понятий и их определений,
разделенных знаком тире.
После заполнения словаря программе передается натуральное число m – количество запросов,
а затем m строк, каждая из которых представляет собой одно понятие.
Если это понятие есть в словаре, необходимо вывести его определение,
в обратном случае – "Не найдено".
"""
def dot_input():
    while True:
        s = input()
        if s == ".":
            break
        else:
            s = s.split(" – ")
            return s

def rezult():
    m = int(input())
    vvod = [input() for x in range(m)]

    for x in range(m):
        if vvod[x] in vok:
            print(vok[vvod[x]])
        else:
            print("Не найдено")

def make_work():
    vok = {}
    while True:
        s = input()
        if s == ".":
            rezult()
        else:
            s = s.split(" – ")
            # vok=dict([s])
            vok.update([s])
    return vok


vok = {}
while True:
    s = input()
    if s == ".":
        m = int(input())
        vvod = [input() for x in range(m)]
        for x in range(m):
            if vvod[x] in vok:
                print(vok[vvod[x]])
            else:
                print("Не найдено")
    else:
        s = s.split(" – ")
        vok.update([s])
