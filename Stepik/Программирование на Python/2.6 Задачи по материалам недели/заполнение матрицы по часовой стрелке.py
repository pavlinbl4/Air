# n = int(input())
n = 5
a = []
count = 10
# создаю матрицу заполненную нулями или другим символом
for i in range(n):
    a.append(["**"]*n)


# заменяю нули по правилу
st = 0
for i in range(n):
    if i == st:
        for j in range(n-st):
                count += 1
                a[i][j] = count
    elif 0 < i < n - 1 - st:
            count += 1
            a[i][n- 1 - st] = count
    elif i == n - 1 - st :
        for j in range(n-1-st,-1,-1):
                count += 1
                a[n-1-st][j] = count
st  = st +1
for i in range(n - 1 - st, 0, -1):
    count += 1
    a[i][st - 1] = count



for i in a:

    print(*i)