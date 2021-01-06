file = open('/Users/evgeniy/Downloads/numbers.txt')
count_3_digit = 0
sum_2_digits = 0
for row in file:
    if len(row) == 4:
        print(row)
        count_3_digit += 1
    if len(row) == 3:
        sum_2_digits += int(row)
print(count_3_digit,sum_2_digits,sep=",")

