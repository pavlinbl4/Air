def file_read(file_name):
    file = open(file_name, encoding='utf-8')
    print(file.read())
    # print(file_name)


file_read("test.txt")