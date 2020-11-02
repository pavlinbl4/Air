def print_goods(*args):
    n = 0
    for i in args:
        if str(i) in args and i != "":
            n += 1
            print(n,i,sep=". ")
    if n == 0:
        print("Нет товаров")





print_goods('apple', 'banana', 'orange')