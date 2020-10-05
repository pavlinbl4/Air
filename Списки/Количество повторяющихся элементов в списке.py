""" найти количество повторяющихся элементов в списке и создать словарь
"""
voc = {}
vv = [4, 5, 5, 12]

# вариант 1
# for i in vv:
#     voc[i] = vv.count(i)
# print(voc)


# варианте 2
# voc = dict((x,vv.count(x)) for x in vv)
# print(voc)

# вариант 3
from collections import Counter
voc = Counter(vv)
print(voc)