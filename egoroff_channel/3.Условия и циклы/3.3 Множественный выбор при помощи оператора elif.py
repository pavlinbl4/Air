a = float(input())
b = float(input())
s = input()
if s == "/" and b == 0:
    print("Неизвестно")
elif s == "+":
    d = (a+b)
    print(int(d))
elif s == "-":
    d =(a-b)
    print(int(d))
elif s == "*":
    d = (a*b)
    print(int(d))
elif s == "/" and b !=0:
    d = ((a/b))
    print(d)


else:
    print("Неизвестно")







# a,b,c = int(input()),int(input()),int(input())
# if a == b and a == c:
#     print(3)
# elif a == b and a != c:
#     print(2)
# elif a == c and a != b:
#     print(2)
# elif b == c and a != b:
#     print(2)
# else:
#     print(0)