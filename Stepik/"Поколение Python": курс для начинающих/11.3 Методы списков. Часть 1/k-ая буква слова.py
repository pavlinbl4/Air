# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(input())
# k = int(input())
lst = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij']
k = 2
letters = ""
for x in lst:
    if len(x) >= k:
        print(x[k-1])
        letters += x[k-1]
print(type(letters))

        