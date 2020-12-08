n,m = map(int,input().split())

lst_n = [int(i) for i in input().split()]
lst_m = [int(i) for i in input().split()]
# n, m = 2 , 5
# lst_n = [3, 7]
# lst_m = [1, 1, 3, 6, 8, 11, 15, 100]
# xx = min([n,m])
#
# i = 0
rez =[]
while len(lst_m) != 0 and len(lst_n) != 0:
    if lst_n[0] < lst_m[0]:
        rez.append(lst_n[0])
        lst_n.pop(0)
    else:
        rez.append(lst_m[0])
        lst_m.pop(0)
if len(lst_m) != 0:
    for i in lst_m:
        rez.append(i)
else:
    for i in lst_n:
        rez.append(i)

print(rez)
# print(lst_m)
# print(lst_n)





# while i < 5:
# min = lst_m[0]
# print("min =", min)
# if lst_n[0] < lst_m[0]:
#     min = lst_n[0]
#     lst_n = lst_n.remove(min)
# else:
#     lst_m = lst_m.remove(min)
# rez.append(min)
# print(rez)
# print(lst_n)
# print(lst_m)
# i += 1
