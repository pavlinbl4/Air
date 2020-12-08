# объявление функции
def is_palindrome(text):
    text = text.lower()
    text = text.replace("-", "")
    text = text.replace(" ", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    flag = True
    for i in range(len(text) // 2):
        if text[i] == text[-i - 1]:
            flag = True
        else:
            flag = False
            break
    return flag
print(is_palindrome('BEEGEEK'))