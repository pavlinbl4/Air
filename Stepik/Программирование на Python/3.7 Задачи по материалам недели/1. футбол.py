# n = int(input())
# games = []
# for i in range(n):
#     lst = (input().split(";"))
#     games.append({lst[x-1]:int(lst[x]) for x in range(1,len(lst),2)})
# print(games)
games = [{'Спартак': 9, 'Зенит': 10}, {'Локомотив': 12, 'Зенит': 3}, {'Спартак': 8, 'Локомотив': 15}]
# teams = set()
# for i in games:
#     for x in i:
#         teams.add(x)
teams = {'Зенит', 'Локомотив', 'Спартак'}
# print(teams)
# rez = dict.fromkeys(teams,[])
# print(rez)
# rez = {'Зенит': [], 'Спартак': [], 'Локомотив': []}
rez = {'Локомотив': [], 'Зенит': [], 'Спартак': []}

def itog_of_game(komanda):
    lst = list(komanda.items())
    best_team = None
    if lst[0][1] > lst[1][1]:
        best_team = lst[0][0]
    elif lst[0][1] < lst[1][1]:
        best_team = lst[1][0]
    else:
        best_team = "draw"
    return best_team

for komanda in teams: # проверяю каждую команду на ее участие в игре
    count = 0
    victory = 0
    draw = 0
    losing = 0
    ball = 0
    for x in games:
        if komanda in x:
            best_team = itog_of_game(x)
            if best_team == 'draw':
                draw += 1
                # continue
            elif komanda == best_team:
                victory += 1
            elif komanda != best_team:
                losing += 1
            count +=1
    print(komanda,rez[komanda])
    rez[komanda].append(count)
    print(rez)
    # rez[komanda].append(victory)
    # rez[komanda].append(draw)
    # rez[komanda].append(losing)
    # rez[komanda].append(victory*3 + draw)
# print(rez)
# for i in rez:
#     print(i+":"+ " ".join(map(str,rez[i])))
    # print(i+":",*rez[i])
    # print(rez)



