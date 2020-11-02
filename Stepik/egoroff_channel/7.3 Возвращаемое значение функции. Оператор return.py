def factorial(n):
    pr = 1
    for i in range(2,n+1):
        pr = pr*i
    return pr
n = int(input())
# print(factorial(n))
factorial(n)