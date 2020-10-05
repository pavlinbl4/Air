# roman_to_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# numb = input()  # Формат ввода: Строка, содержащая натуральное число
numb = 1984

# преобразуем готовый словарь наоборот
# dec_to_roman = {}
# for x in roman_to_dec:
#     dec_to_roman[roman_to_dec[x]] = x
# print(dec_to_roman)

dec_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
# print(len(str(numb))) # узнаю количество знаков в числе
vv = []
for i in range(len(str(numb))):
    vv.append(int((numb%10 * (10**(i+1)))/10))
    numb = numb//10
for i in range(len(vv)-1,-1,-1):
    print(vv[i])
