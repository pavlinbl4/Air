n = int(input())
if n == 1:
    print(0)
else:
    count = 0
    if n % 2 == 0:
        # print("even")
        while n != 1:
            n = n /2
            count += 1
            if n % 2 == 1 and n != 1:
                count = 0
                break
    if count == 0:
        print("НЕТ")
    else:
        print(count)








