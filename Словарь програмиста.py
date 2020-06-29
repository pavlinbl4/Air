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
print(dot_input())



