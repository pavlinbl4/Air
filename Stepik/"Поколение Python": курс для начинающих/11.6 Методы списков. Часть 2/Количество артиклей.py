txt = input().lower().split()
print("Общее количество артиклей:",txt.count('a') + txt.count('an') + txt.count('the'))
