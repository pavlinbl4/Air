s ="Посоветуй мне книгу (Maria)" # преобразовать в список , где имя в скобках и фраза разные строки

s = s.split(" (")
print(s[1][:-1])
s[1] = s[1][:-1]
print(s)
print()
print()

b = 'Dontsova "Десять негритят"'
print(b)
b  = b.split(' "')
b[1] = b[1][:-1]
print(b)
