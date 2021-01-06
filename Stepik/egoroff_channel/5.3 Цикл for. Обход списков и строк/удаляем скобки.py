lst = ['{', ']', ']', '[', ']', ']', '(', ')']
l = len(lst)
x = 0
while l > 0 and x < l:
    if lst[x] == "[" and lst[x+1] == "]" or lst[x] == "(" and lst[x+1] == ")":
        lst.pop(x)
        lst.pop(x)
        l -= 2
        x = 0
        continue
    x +=1



print(lst)