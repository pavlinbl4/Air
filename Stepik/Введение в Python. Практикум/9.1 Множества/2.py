# a1 = set(input().split(", "))
# a2 = set(input().split(", "))
a1 = set("Trista Macmaster, Gigi Wall, Rosamond Boan".split(", "))
a2 = set("Roselee Mayhan, Rosamond Boan, Malik Madore, Keena Kopf, Trista Macmaster, Cortez Mestas, Barbar Mease, Elease Knudson, Chas Nevius, Serafina Shemwell".split(", "))
b = set.intersection(a1,a2)
print(*b,sep=", ")
