n, m = map(int,input().split())
a = [] # исходный массив данных
for i in range(n):
    a.append(list(map(int,input().split())))

s = []  # список лучших бросков у каждого спортсмена
for x in range(n):
    s.append(max(a[x]))
# print("список лучших бросков у каждого спортсмена - ", s)

# print(max(s)) # самый лучший результат из списка лучших бросков
# print("количество максимальных результатов - ",s.count(max(s))) # количество максимальных результатов

if s.count(max(s)) == 1: # количество максимальных результатов  - один выводим номер игрока
    print(s.index(max(s))) # номер спортсмена с наилучшим результатом
else: # если у нескольких спортсменов лучший результат
    best_sportman = [] # номера спортсменов с лучшим результатом
    sum_all = [] # сумма бросков у лучших спортсменов
    for x in range(s.count(max(s))):
        # best_sportman.append(s.index(max(s), s.index(max(s)) + x))
        best_sportman.append(s.index(max(s)) + x)
        # sum_all.append()
        # print(sum(a[]))
    # print('номера лучших спортсменов -', best_sportman)
    for i in best_sportman:
        sum_all.append(sum(a[i]))
    # print("суммарный результат лучших спортсменов - ",sum_all)
    print(best_sportman[sum_all.index(max(sum_all))])





