n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
s = []
# print(a)# исходный массив
for x in range(n):
    s.append(max(a[x]))
# print(s) #максимальное значение в каждом списке
# print(max(s)) #самое большое значение из всех в массиве
# print(s.count(max(s)))
dd = s.count(max(s)) # количество одинаковых максимумов
# print(dd)
mm = []
if dd > 1: # если максимальные значения повторяются
    for x in range(dd):
        mm.append(sum(a[s.index(max(s),s.index(max(s))+x)]))
    print(mm)
    VVV = mm.index(max(mm))
else:
    VVV = a.index(a[s.index(max(s))])
print(VVV)
