data =[]
itog = []
n = 0
while True:
    xxx = input()
    # print(xxx)
    if xxx != "end":

        data.append([int(i) for i in xxx.split()])
        n += 1
    else:
        # print(data)
        for i in range(len(data)):
            print(*data[i])

        # выводим результирующую матрицу
        for i in range(len(data)):
            for j in range( len(data[0])):
                itog.append(data[i][j])

        break

print("*"*50)
for i in range(len(data)):
    print()
    for j in range(len(data[0])):
        print(itog[i][j])




