lst = []
while True:
    w = input()
    if w == ".":
        print(lst)
        break
    else:
        lst.append(w.split())