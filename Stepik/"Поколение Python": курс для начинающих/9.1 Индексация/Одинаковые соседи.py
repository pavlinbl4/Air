st = input()
count = 0
for i in range(len(st)-1):
    if st[i] == st[i+1]:
        count +=1
print(count)

