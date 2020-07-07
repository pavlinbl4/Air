"""если в предложениее встречается слово, начинающееся на "фу" два раза подряд,
то вывести "плохо" если нет "пофукай еше"."""
s =" кунгфу 1Фуфловая Фура обогнала фургон" # пример ввода
s = s.lower().replace(",","").replace(".","").replace("!","").replace("-","").split()
z = 0
for x in range(len(s)-1):
    if s[x].startswith("фу") == True and s[x+1].startswith("фу") == True:
        print("плохо")
        z = 0
        break
    else:
        z =+1
if z != 0:
    print("пофукай еше")