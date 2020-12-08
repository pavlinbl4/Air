skrip = set(input().split(", "))
nem = set(input().split(", "))
print(*skrip.difference(nem),sep=", ")