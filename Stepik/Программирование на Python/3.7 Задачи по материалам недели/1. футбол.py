# n = int(input())
# # lst = []
# voc = {}
# for i in range(n):
    # lst.append(input().split(";"))
# print(lst)

lst = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
teams = set()
for i in lst:
    teams.add(lst[i][0])
    teams.add(lst[i][2])
print(teams)
