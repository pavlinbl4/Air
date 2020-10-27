n, k = map(int,input().split())
t = 0
count = 0
while t <= 240 - k and count <= n:
    count += 1
    t = t + count * 5
    # print( "tasks -", count," ","time -",t)

print(count-1)