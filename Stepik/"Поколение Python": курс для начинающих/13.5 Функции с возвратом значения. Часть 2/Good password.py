# объявление функции
def is_password_good(password):
    if len(password) >= 8:
        lower = 0
        digit = 0
        upper = 0

        for i in password:
            if i.islower() == True:
                lower = 1
            elif i.isdigit() == True:
                digit = 1
            elif i.isupper() == True:
                upper = 1

        if lower > 0 and digit > 0 and upper >0:
            return True
        else:
            return False
    else:
        return False




# считываем данные
# txt = input()

# вызываем функцию
print(is_password_good('abchfgggggGg'))