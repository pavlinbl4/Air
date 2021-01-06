# a = [ 'a','b','c','d','e','f','g','h']
# cod = {a[x-1]:x for x in range(1,len(a)+1)}
# # print(cod)
# point1,point2 = input(),input()
# point1 = [point1[0],int(point1[1])]
# point2 = [point2[0],int(point2[1])]
# if ((cod[point1[0]] + point1[1])%2 == 0 and (cod[point2[0]] + point2[1])%2 == 0) or (cod[point1[0]] + point1[1])%2 != 0 and (cod[point2[0]] + point2[1])%2 != 0:
#
#     print("YES")
# else:
#     primt("NO")
# # print(point1)
# # print

print(list(map(ord, input())))
