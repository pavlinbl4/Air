# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c


    if d == 0:
        return -b / (2 * a),-b / (2 * a)
    elif d > 0:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)

x1, x2 = solve(1, 2, 1)
print(x1, x2)
# print(solve(-2, 7, -5))
