n, m = map(int,input().split())
a = [] # исходный массив данных
for i in range(n):
    a.append(list(map(int,input().split())))

s = []  # список лучших бросков у каждого спортсмена
for x in range(m):
    s.append(max(a[x]))


print(max(s)) # самый лучший результат из списка лучших бросков
print(s.count(max(s))) # количество максимальных результатов
dd = s.count(max(s)) # количество одинаковых максимумов
# print(dd)
# print(s.index(max(s)))# НОМЕР ИГРОКА С ЛУЧШИМ БРОСКОМ ЕСЛИ ОН ОДИН
mm = [] # сумма результатов у лучших игроков
if dd > 1: # если максимальные значения повторяются
     for x in range(dd):
         mm.append(sum(a[s.index(max(s),s.index(max(s))+x)]))
     print(mm)
     VVV = mm.index(max(mm))
# else:
#     # VVV = a.index(a[s.index(max(s))])
# #
#     VVV = s.index(max(s))
# print(VVV)
