s ="Посоветуй мне книгу (Maria)" # преобразовать в список , где имя в скобках и фраза разные строки

s = s.split(" (")
print(s[1][:-1])
s[1] = s[1][:-1]
print(s)
print()
print()


dict={}
b = 'Dontsova "Десять негритят"'
a = ['Dontsova', '10 негритят']
print(b)
b  = b.split(' "')
b[1] = b[1][:-1]
print(b)
dict=  {b[0]}
# dict[b[b]].append(5555)
# dict = {a[0]:0[a[1]]}
print(dict)
print(dict[Dontsova])



# book =  input().split(", ")
# lybr = {x: book[x] for x in range(len(book))}
# print(lybr)
# print(len(lybr[0]))
# print(book)
# lybr = {}
# for x in range(len(book)):
#
#     book[x] = book[x].split(' (')
#     book[x][1] = book[x][1][:-1]
#     lybr.update([book[x]])
# print(lybr)
