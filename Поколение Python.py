a,b,c = int(input()),int(input()),int(input())
# if a > b and a > c and b + c > a:
#     print("YES")
# else:
#     print("NO")
# if b > a and b > c and a + c > b:
#     print("YES")
# else:
#     print("NO")
# if c > a and c > b and a + b > a :
#     print("YES")
# else:
#     print("NO")
if a + b > c and a + c > b and b + c > a :
    print("YES")
else:
    print("NO")

