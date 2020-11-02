d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = {}
rez.update(d1)
rez.update(d2)
print(rez)
d1.update(d2)
print(d1)