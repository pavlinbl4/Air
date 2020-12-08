# st = "Блажен, кто верует, тепло ему на свете!"
st ="Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
abc = "а, б, в, г, д, е, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я"
abc = abc.replace(", ","")
# print(abc)
# print(len(abc))
ABC = abc.upper()
# print(ABC)
ABCabc = ABC +abc
# print(ABCabc)
n = -7
for i in st:
    # if i.isalpha():
    if i.isupper() and i.isalpha():
        print(ABC[ABC.index(i)+n],end="")
    elif i.islower() and i.isalpha():
        print(abc[abc.index(i)+n],end="")
    else:
        print(i,end="")