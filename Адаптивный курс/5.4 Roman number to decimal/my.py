# st = input()
st = "MCMLXXXIV"
roman_to_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
dec = []
for x in st:
    dec.append(roman_to_dec[x])
# print(dec)
z = 0
# for x in range(len(dec)-1,-1,-1):
while len(dec) != 1:
    if dec[0]>=dec[1]:
        z = z +  dec.pop[0]
    else:
        dec[1] = dec[1] -dec[0]
        dec.pop[0]
print(z)