"""нужно вывести список без скобок и запятых, между элементами списка толжны быть знаки табуляции
"""

lst = ['— •••• •', '——•— ••— •• —•—• —•—', '—••• •—• ——— •—— —•', '••—• ——— —••—', '•——— ••— —— •——• •••', '——— •••— • •—•', '— •••• •', '•—•• •— ——•• —•——', '—•• ——— ——•']
print([x for x in lst])
print("\t".join(lst))
print("$$$$$".join(lst))