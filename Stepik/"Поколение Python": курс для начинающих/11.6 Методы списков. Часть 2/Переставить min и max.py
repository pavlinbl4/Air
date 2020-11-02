lst = list(map(int,input().split()))

max_digit = max(lst)

max_index = lst.index(max_digit)
min_digit = min(lst)
min_index = lst.index(min_digit)
lst[max_index] = min_digit
lst[min_index] = max_digit
print(*lst)