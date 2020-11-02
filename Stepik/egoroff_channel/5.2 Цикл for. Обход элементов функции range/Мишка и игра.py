n = int(input())
rez = []
for i in range(n):
    m , c = map(int,input().split())
    rez.append( m - c)
if sum(rez) > 0:
    print("Mishka")
elif sum(rez) < 0:
    print("Chris")
else:
    print("Friendship is magic!^^")