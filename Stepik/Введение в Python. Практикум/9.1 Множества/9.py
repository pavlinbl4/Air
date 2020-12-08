lst = [("Ivan", "Maria"),
         ("Ella", "Ivan"),
         ("Ivan", "Oleg")]
# print(lst[0])
# print(len(lst))
all = set()
for x in range(2):
    all.update(i[x] for i in lst)
print(all)