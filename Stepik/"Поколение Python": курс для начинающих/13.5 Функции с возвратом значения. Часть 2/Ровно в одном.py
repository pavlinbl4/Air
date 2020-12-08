# объявление функции
def is_one_away(word1, word2):
    flag1 = True
    count = 0
    if len(word1) == len(word2):
        flag1 = True
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        if len(word1) - count == 1:
            return True
        else:
            return False


    else:
        return False



print(is_one_away('abcd', 'abcde'))