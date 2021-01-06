def longest_word_in_file(file_name):

    file = open(file_name, encoding="utf-8")
    max_word =""
    for row in file:
        words = row.split()
        for word in words:
            word = remove_punctuation(word)
            if len(word) >= len(max_word):
                max_word = word
    return max_word

def remove_punctuation(word):
    from string import punctuation
    for i in punctuation:
        if i in word:
            word = word.replace(i,"")
    return word

print(longest_word_in_file("test.txt"))