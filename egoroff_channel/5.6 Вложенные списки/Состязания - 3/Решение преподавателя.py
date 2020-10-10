n, m = map(int,input().split())
a = [] # исходный массив данных
for i in range(n):
    a.append(list(map(int,input().split())))

max_score = 0
max_summa = 0
max_index = 0

for row in range(n):
    max_try = 0
    s = 0
    for colum in range(m):
        s += a[row][colum]
        if a[row][colum] > max_try:
            max_try = a[row][colum]
    # print("--" * 50)
    if max_try > max_score:
        max_score = max_try
        max_summa = s
        max_index = row
    elif max_try == max_score and s > max_summa:
        max_score = max_try
        max_summa = s
        max_index = row
# print("ряд - ", max_index, "максимальный результат - ",max_score, "сумма результатом -",max_summa )
# print("*" * 50)
print(max_index)
