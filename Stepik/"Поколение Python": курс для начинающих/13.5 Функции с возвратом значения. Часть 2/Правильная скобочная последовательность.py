# объявление функции
def is_correct_bracket(text):
    if text[0] == "(" and text.count("(") == text.count(")"):
        count = 0
        for i in text:
            if i == "(" or i == ")":
                count += 1
        if count == len(text):
            return True
        else:
            return False
    else:
        return False

print(is_correct_bracket('()(())()'))