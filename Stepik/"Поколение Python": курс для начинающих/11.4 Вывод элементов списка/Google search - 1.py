lst =[]
for i in range(int(input())):
    lst.append(input())
ss = input().lower()
print(lst)
for x in lst:
    if ss in x.lower():
        print(x)