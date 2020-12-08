# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    num += 1
    while is_prime(num) == False:
        num += 1
        is_prime(num)
    return num


# считываем данные
# n = int(input())

# вызываем функцию
print(get_next_prime(174))