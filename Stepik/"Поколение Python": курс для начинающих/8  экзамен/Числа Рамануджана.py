xx = set()
lst =[]
for x in range(5):
    for a in range(1,40):
        for b in range(1,40):
            for c in range(1,40):
                for d in range(1,40):
                    if a ** 3 + b **3 == c ** 3 + d ** 3  and a != b and a != c  and a!= d and b != c and b != d and c != d and a < b and c < d:
                        print( a**3 + b** 3, "a = ", a, "b = ",b, "c = ", c, "d = ",d)
                        lst.append(a**3 + b** 3)
lst = sorted(lst)
# xx.add(lst)
print(lst)
