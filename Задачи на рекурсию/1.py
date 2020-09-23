"""
Дано натуральное число n. Выведите все числа от 1 до n.
"""

n = 4
def nat(n):
    if n == 0:
        return n
    print(n)
    return nat(n-1) + n
# print(nat(n))
nat(n)

