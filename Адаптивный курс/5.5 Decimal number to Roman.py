roman_to_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dec_to_roman = {}
for x in roman_to_dec:
    dec_to_roman[roman_to_dec[x]] = x
print(dec_to_roman)