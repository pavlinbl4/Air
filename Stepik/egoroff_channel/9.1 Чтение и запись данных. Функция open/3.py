def longest_word_in_file(file_name):
    from string import punctuation
    file = open(file_name, encoding="utf-8")
    long_name = {}
    all_words = []
    lst = file.readlines()
    for line in lst:
        line.replace("\n","")
        for letter in line:
            if letter in punctuation:
                x = letter
                line = line.replace(x," ")
        # print(line.split(" "))
        for word in line.split(" "):
            all_words.append(word)
            # print(word, "---", type(word),"----",len(word))
            # long_name.setdefault(len(word),word)
    # print(long_name)
    # print(max(sorted(long_name)))
    # print(long_name[max(sorted(long_name))])
    print(all_words)


longest_word_in_file("test.txt")