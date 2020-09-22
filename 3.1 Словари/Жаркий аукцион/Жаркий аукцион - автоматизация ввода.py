# вводятся изначальные данные
# items = input().split(", ") # список предметов
items = ['Apple II', 'компьютерная мышь Lisa', 'Sony PS1', 'YIS-805', 'IBM 5150', 'Macintosh LC520', 'Эльбрус 801-PC']
# price = int(input())
price = 1500
# buyers = input().split(", ") # список покупателей
buyers = ['Michael', 'Jake', 'John', 'Alex', 'Jane', 'Steve']
vvod = """John YIS-805 400
Jane Macintosh LC520 5000
Jake Macintosh LC520 4000
Michael IBM 5150 10000
Alex Apple II 1501000
BobDilan Apple II 77777
BobDilan Apple II 77777
Steve Apple II 15000
Sergey Apple II 17000
Lisa компьютерная мышь Lisa 5000
Jake Sony PS1 4200
BobDilan Apple II 77777
Аукцион закончен!
END"""
lot = {} # словарь ключ покупатель и ставка - значение предмет
userbid = {}
xx = vvod.splitlines()
for x in range(len(xx)):
    if xx[x] == "END":
        break
    else:
        bid = xx[x]
        if bid == "Аукцион закончен!":
            for i in items:
                if i not in lot:
                    print(i, "Предложений не было")
                else:
                    print(max(lot[i]))
                    print(i,lot[i][max(lot[i])],max(lot[i]) )
            break
        else:
            if bid.split()[0] in buyers and int(bid.split()[-1]) > price:
                u = bid.split()[0]
                money = bid.split()[-1]
                lot.setdefault(" ".join(bid.split()[1:-1]),{})
                lot[" ".join(bid.split()[1:-1])].update({int(money):u})
    print(lot)# словарь где ключ предмет, а значение словарь со ставками






