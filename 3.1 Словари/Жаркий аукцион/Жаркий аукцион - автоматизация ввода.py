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
Alex Apple II 1501
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
            print("REZULT")
            break
        else:
            # print("Имя участника - ", bid.split()[0])
            # print("Размер ставки - ", bid.split()[-1])
            # print("Название предмета - ", " ".join(bid.split()[1:-1]))
            if bid.split()[0] in buyers and int(bid.split()[-1]) > price:
                print("участник - ", bid.split()[0], ", предмет - "," ".join(bid.split()[1:-1]),", ставка - ", bid.split()[-1])
                # u = bid.split()[0]
                # print(u)
                # it = " ".join(bid.split()[1:-1])
                # print(it)
                # money = bid.split()[-1]
                # print(money)
                # print((lot.fromkeys(u,money)))
                userbid[bid.split()[-1]] = bid.split()[0]
                print(userbid)
                lot.setdefault(" ".join(bid.split()[1:-1]),{})
                lot[" ".join(bid.split()[1:-1])].update(userbid)
                # lot[" ".join(bid.split()[1:-1])].append(bid.split()[-1])
                # lot[" ".join(bid.split()[1:-1])] = [bid.split()[0],bid.split()[-1]]
    print(lot)






            # else:
            #     print("либо ставка маленькая, либо участник не зарегестрирован")










# items = xx[0].split(", ")  # список предметов
# price = int(xx[1])  # начальная стоимость всех предметов
# buyers = xx[2].split(", ") # список покупателей
# print('\n',items,'\n',price,'\n',buyers)