rez=[]
n = "3ab4c2Ca777B"
x = 0
while x < len(n):
    if n[x].isalpha() == True:# если буква
        rez.append(n[x])
        x+=1
    else: # если цифра
        if n[x+1].isalpha() == True: # следом за цифрой буква
            b = int(n[x])*n[x+1]
            rez.append(b)
            x+=2
        else: # снова цифра
            z = int(n[x])*10+int(n[x+1])
print("".join(rez))