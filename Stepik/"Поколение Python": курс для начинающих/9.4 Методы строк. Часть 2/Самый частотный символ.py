txt = input()
max = 0
simbol = 0
for i in txt:
    if txt.count(i) >= max :
        max = txt.count(i)
        simbol = i
print(simbol)

