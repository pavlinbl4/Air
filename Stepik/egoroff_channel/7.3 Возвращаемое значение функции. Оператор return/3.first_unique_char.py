def first_unique_char(x):
    for i in range(len(x)):
        # print(x[i],'++++',x.find(x[i]),"----",x.rfind(x[i]))
        if x.find(x[i]) == x.rfind(x[i]):
            return i

    return -1


x = "abracadabra"
print(first_unique_char(x))
# first_unique_char(x)