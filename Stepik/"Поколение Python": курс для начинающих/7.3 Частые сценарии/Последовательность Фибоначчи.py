n = int(input())
# if n == 1 or n == 2:
#     print(1)
# else:
fib1 = 1
fib2 = 0
fib = 0
while n > 0:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    n -= 1
    print(fib,end = " ")
