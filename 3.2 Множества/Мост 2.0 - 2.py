lang = [set(input().split(", ")) for x in range(int(input()))]
[lang[0].intersection_update(x) for x in lang[1:]]
print(*lang[0] if len(lang[0]) != 0 else ["Фильм снять не удастся:("], sep =", ")