"""
данная задача возникла в рамках решения задачи Bookflix
есть список жанров книг, нужно выбрать любимый, те наиболее часто повторяющийся
"""
jan = ['детектив', 'фантастика','ужасы','ужасы', 'детектив']
sort_jan ={}# словарь где будет жанр и количество повторов
for x in range(len(jan)):
    ss = jan.count(jan[x])
    sort_jan[jan[x]] = ss
print(sort_jan)
print(max(sort_jan,key=sort_jan.get))
print(list(sort_jan))
for nnn in list(sort_jan):
    print(nnn)
print()

