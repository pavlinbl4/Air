n = int(input())
a = []
for i in range(n):
    # a.append(list(map(int,input().split()))) создаем массив из чисел
    a.append(input().split()) # созаем массив из строк
count = 0
for i in range(n):
    # print("первый столбец - ", a[i][0])
    x = a[i][0]
    for i in range(n):
        y = a[i][1]
        # print("второй стобец - ", a[i][1])
        # if a[i][0] == a[i][1]:
        if x == y:
            count +=1
print(count)






    # for j in range(n):
    #     print("первый столбец - ",a[i][j], "второй стобец - ", a[i][j])
