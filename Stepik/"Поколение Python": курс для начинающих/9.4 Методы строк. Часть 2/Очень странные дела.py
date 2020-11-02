n = int(input())
count = 0
for x in range(n):
    txt = input()
    if txt.count("11") >= 3:
        count += 1
print(count)