"""На вход программе подается текст. Выведите слово (в нижнем регистре), которое встречается в тексте чаще всего,
и количество его появлений через пробел. Гарантируется, что из знаков препинания встречаются только символы
{",", ".", "?", "!"}, а также то, что в тексте есть только одно слово с наибольшей частотой появлений."""

text = input()
# text = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"
text = text.lower().replace(",","").replace(".","").replace("?","").replace("!","").split(" ")
# text = text.replace(",","")
# text = text.replace(".","")
# text = text.replace("?","")
# text = text.replace("!","")
# text = text.split(" ")
# n = len(text)
# print(text, n, type(text))
# for x in text():
# words = {x:text[x] for x in range(len(text))}
# print(words)
# print(words.values())
# print(words.items())
# print(iter(words.keys()))
dct = {}
for x in text:
    dct[x] = dct.get(x,0) +1
m = max(dct.values())
print(*[ key for key, val in dct.items() if val == m],m)