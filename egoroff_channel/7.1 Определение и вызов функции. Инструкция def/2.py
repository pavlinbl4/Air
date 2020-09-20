def check_password(n):
    z = 0
    w = 0
    k = 0
    a = "!@#$%*"
    for i in n:
        if i.isdigit():
            k+=1
    for x in n:
        if x.isupper():
            z = 1
    for y in n:
        if y in a:
            w = 1
    if len(n) > 10 and  w == 1 and z == 1 and k>=3:
        print("Perfect password")
    else:
        print("Easy peasy")



check_password("qQwerty1357!")

