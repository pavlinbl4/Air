# dd ={"Фича" : "недокументированная дополнительная возможность, фишка"}
# if ",jkn" in dd:
#     print(dd["Фича"])
# else:
#     print("fuck")

vok = {"Фича" : "недокументированная дополнительная возможность, фишка"}
m = 4
vvod = [input() for x in range(m)]
for x in range(m):
    if vvod[x] in vok:
        print(vok[vvod[x]])
    else:
        print("Не найдено")
