skrip = set(input().split(", "))
nem = set(input().split(", "))
print(*skrip.symmetric_difference(nem),sep=", ")