def create_file_with_numbers(n):
    file = open(f'range_{n}.txt','w')
    # lst = [i for i in range(1,n+1)]
    # file.write(" ".join(str(i) for i in lst))
    for i in range(1,n+1):
        file.write(str(i)+"\n")
    file.close()


create_file_with_numbers(6)