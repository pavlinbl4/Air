n = int(input())
# digit = []
# while n > 0:
#     digit.append(n % 2)
#     n = n // 2
# digit = reversed(digit)
# print(*digit,sep="")

digit = ""
while n > 0:
    digit = digit + str(n % 2)
    n = n // 2
print(digit[::-1])
