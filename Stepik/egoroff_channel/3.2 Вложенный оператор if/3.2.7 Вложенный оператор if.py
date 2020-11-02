n = "Тверa" #input()
m = "Aоттердамь" #input()
if n[-1] == 'ь':
    n = n[0:-1]
if n[-1] == m[0].lower():
    print("Good")
else:
    print("Bad")
# if n[-1] == "ь":
#     if n[-2] == m[0].lower():
#         print("Good")
#     else:
#         print("Bad")
# else:
#     if n[-1] == m[0].lower():
#         print("Good")
#     else:
#         print("Bad")