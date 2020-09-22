n = "Лондонь" #input()
m = "Норильск" #input()
if n[-1] == "ь":
    if n[-2] == m[0].lower():
        print("Good")
    else:
        print("Bad")
else:
    if n[-1] == m[0].lower():
        print("Good")
    else:
        print("Bad")