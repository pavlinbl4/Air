test = { 'a': '03.08.2019', 'b' : '23.07.2019', 'c' : '28.09.2019'}
# преобразовать даты в списке с числами
for i in test:
    # print(test[i])
    print(list(map(int,test[i].split("."))))
    test[i] = list(map(int,test[i].split(".")))
print(test)
# for i in test:
#     if test[i][2]
