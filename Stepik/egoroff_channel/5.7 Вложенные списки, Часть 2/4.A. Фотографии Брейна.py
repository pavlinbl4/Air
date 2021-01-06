n,m = map(int,input().split())
count = 0
for i in range(n):

    line = input().split()
    if "C" in line or "M" in line or "y" in line:
        print("#Color")
        count += 1
        break
if count == 0:
    print("#Black&White")


