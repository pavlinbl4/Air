x = int(input()
p = int(input()    # процент прироста
y = int(input()       # достижение
count = 1

while x <= y:
    print( "day", count, "-----", "distance",x)
    count += 1
    x = x + x/100*p

print(count)