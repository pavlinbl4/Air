"""
дан словарь, где ключи слова, значения целые числа,
нужно найти ключ у которого наибольшее числовое значение

"""

k = {'Спартак': 10, 'Зенит': 10}
lst = list(k.items())
best_team = None
if lst[0][1] > lst[1][1]:
    best_team = lst[0][0]
elif lst[0][1] < lst[1][1]:
    best_team = lst[1][0]
else:
    best_team = "draw"

print(best_team)
