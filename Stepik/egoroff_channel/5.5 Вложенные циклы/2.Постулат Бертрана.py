n = int(input())
count = 0
for i in range(n+1,2*n):
    if i % 2 != 0:
        flag = 1
        for j in range(2,i):
            if j**j < i:
                if i % j == 0:
                    flag = 0
                    break
        if flag == 1:
            count += 1
print(count)