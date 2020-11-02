n = int(input())
def fib_numb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_numb(n -1) + fib_numb(n-2)




print(fib_numb(n))
