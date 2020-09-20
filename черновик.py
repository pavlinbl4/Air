# m = "world"
# b = "slon"
# print(b+"\n"+m)
#
#
# n = 5
# print(str(n)+"\n"+str(n+1)+"\n"+str(n+2))
#
# print(f"Следующее за числом {n} число: {n+1}" )
#
# a, b = 5 , 9
# print( str(a) + "+" + str(b) + "=" + str(a+b))
#
# a = 82 // 9 % 7
# print(a)


# x = 3
# y = 4
# z = x + y
# z = z + 1
# x = y
# y = 5
# x = z + y + 7
# print(x)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c = int(input()), int(input()), int(input())
# a, b = int(input()), int(input())

# n = int(input())

# a = 2 #n//1000
# b = 7 #n//100%10
# c = 5 #n//10%10
# d = 4 #n%10
# min1 = 0
# min2 = 0
# if a < b:
#     min1 = a
# else:
#     min1 = b
# if c < d:
#     min2 = c
# else:
#     min2 = d
# if min1 < min2:
#     print(min1)
# else:
#     print(min2)

# n = int(input())
# a, b, c = int(input()), int(input()), int(input())
# s = 0
# if a > 0:
#     s = s + a
# if b > 0:
#     s = s + b
# if c > 0:
#     s = s + c
# print(s)


a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)


