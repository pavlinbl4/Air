# x = "6311 9423 142 142 8654 909 Error 6311 142 909 404 502 828 404 9423"
# print(x)
# print(len(x.split()))
# print("*" *100)
# print(len(set(x.split())))
# print(len(input().split()))
x = input()
print(len(x.split())-len(set(x.split())))