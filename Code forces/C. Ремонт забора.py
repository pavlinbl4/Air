l = int(input()) # максимальный размер щита
n = int(input()) # количество досок в заборе
a = [] #['1', '1', '1', '1', '1', '1', '1', '1'] #
# print(type(a[0]))
for x in range(n):
    a.append(input())
count = 0
z = a.count('1') # сколько всего плохих досок
while z > 0:
    d1 = a.index("1") # первая плохая доска
    rem = list(a[d1:d1+l])# участок, который закроет щит
    zz = rem.count("1") # сколько плохих досок закрыл щит
    z -= zz # вычитаю отремонтированные доски
    for i in range(zz):
        a.remove("1")
    count += 1 # считаю использованные щиты
print(count)
# print("Потребуется щитов - ",count)
