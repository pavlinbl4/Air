def  find_duplicate(ls):
    dubl = []
    for i in ls:
        if ls.count(i) > 1 and i not in dubl:
            dubl.append(i)
    return dubl


ls = [2,5,6,7,2,8,9,7,6,6,8]
print(find_duplicate(ls))