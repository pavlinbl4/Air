# n = int(input())
# n = 123456
# dl = list(map(int,n[:,4]))
# print(dl)


n = input()
left_n = list(map(int, n[:-3]))
right_n = list(map(int,(n[-3:])))
if sum(left_n) == sum(right_n):
    print("YES")
else:
    print("NO")
print((left_n))
print(right_n)
