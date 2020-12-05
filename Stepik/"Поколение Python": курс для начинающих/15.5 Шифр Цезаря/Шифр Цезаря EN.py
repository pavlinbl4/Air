
st = "To be, or not to be, that is the question!"
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()

n = 17
for i in st:
    if i.isupper() and i.isalpha():
        print(ABC[ABC.index(i)+n],end="")
    elif i.islower() and i.isalpha():
        print(abc[abc.index(i)+n],end="")
    else:
        print(i,end="")sd