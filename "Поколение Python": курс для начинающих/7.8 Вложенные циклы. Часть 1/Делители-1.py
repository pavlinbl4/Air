a, b = int(input()),int(input())
# a = 1
# b = 100
max_del_sum = 0
summa_deliteley = 0
# vok = {}
digit = 0
for i in range(a,b+1):
    # vok [i] = []
    summa_deliteley = 0
    for delitel in range(1,i+1):
        if i % delitel == 0:
            # print("i = ",i,"   ","delitel =", delitel)
            # vok[i].append(delitel)
            summa_deliteley = summa_deliteley + delitel
    # print("i = ", i, "   ", "summa_deliteley =", summa_deliteley)
    if summa_deliteley >= max_del_sum:
        max_del_sum = summa_deliteley
        digit = i


# print(vok)
print(digit, max_del_sum)
