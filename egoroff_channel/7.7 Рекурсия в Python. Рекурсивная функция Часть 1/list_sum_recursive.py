lst = list(map(int,input().split()))

# print(n)
# print(lst)
def list_sum_recursive(lst):
    n = len(lst)
    if n == 1:
        return lst[0]

    return list_sum_recursive(lst[1])









print(list_sum_recursive(lst))