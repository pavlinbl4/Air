def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_palindrome(text):
    flag = True
    text = str(text)
    for i in range(len(text) // 2):
        if text[i] == text[-i - 1]:
            flag = True
        else:
            flag = False
            break
    return flag

def is_valid_password(password):
    test =[int(i) for i in password.split(":")]
    if len(test) != 3:
        return False
    else:
        if is_palindrome(test[0]) != True:
            return False
        elif is_prime(test[1]) != True:
            return False
        elif test[2]%2 != 0:
            return False
        else:
            return True


print(is_valid_password('1221:101:22:22'))