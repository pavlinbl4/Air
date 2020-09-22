def count_letters(n):
    N = len([x for x in n if x.isupper()])
    K = len([x for x in n if x.islower()])
    print( f"Количество заглавных символов: {N}\nКоличество строчных символов: {K}")


count_letters("Привет, Старина")