txt = input()
s = txt.index('h')
e = txt.rindex('h')
print(txt[:s]+txt[e+1:])