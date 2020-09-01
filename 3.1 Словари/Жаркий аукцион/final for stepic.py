# вводятся изначальные данные
items = input().split(", ") # список предметов
price = int(input())
buyers = input().split(", ") # список покупателей
lot = {} # словарь ключ покупатель и ставка - значение предмет
userbid = {}
while True:
    bid = input()
    if bid == "Аукцион закончен!":
        for i in items:
            if i not in lot:
                print(i, "Предложений не было")
            else:
                # print(max(lot[i]))
                print(i,lot[i][max(lot[i])],max(lot[i]))
                # print(i,max(lot[i]), lot[i][max(lot[i])])

        break
    else:
        if bid.split()[0] in buyers and int(bid.split()[-1]) > price:
            u = bid.split()[0]
            money = bid.split()[-1]
            lot.setdefault(" ".join(bid.split()[1:-1]),{})
            lot[" ".join(bid.split()[1:-1])].update({int(money):u})
# print(lot)# словарь где ключ предмет, а значение словарь со ставками






