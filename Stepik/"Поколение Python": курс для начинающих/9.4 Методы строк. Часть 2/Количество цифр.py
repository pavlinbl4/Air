txt = input()
count = 0
for i in txt:
    if i.isdigit() == True:
        count += 1
print(count)