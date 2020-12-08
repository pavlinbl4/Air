ss = [int(i) for i in input().split()]
count = 0
for i in range(len(ss)-1):
    if ss[i] in ss[i+1:]:
        count += ss[i+1:].count(ss[i])
print(count)

