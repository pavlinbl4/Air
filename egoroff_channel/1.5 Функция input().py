a = int(input())
b = int(input())
c = int(input())
s1 = a + b + c
s2 = a * b * c
s3 = a + b * c
s4 = a * b + c
s5 = (a + b) * c
s6 = a * (b + c)
print(max(s1,s2,s3,s4,s5,s6))