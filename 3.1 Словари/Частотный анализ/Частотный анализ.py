n = input()
dd= {}
while True:
    a = input()
    if a == ".":
        break
    else:
        a = a.split(": ")
        dd.update([a])
dd = {v:k for k, v in dd.items()}
print(dd)
for i in range(len(n)):
    if n[i].isalpha():
        x = n.count(n[i])
        x = str(x)
        print(dd[x],end="")

