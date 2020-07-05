letters = [ sumb for sumb in input().lower() if sumb.isalpha()]
dct = {}
for lett in letters:
    dct[lett] = dct.get(lett, 0) +1
max_count = max(dct.values())
result = [ key for key, val in dct.items() if val == max_count]
print(sorted(result)[0])