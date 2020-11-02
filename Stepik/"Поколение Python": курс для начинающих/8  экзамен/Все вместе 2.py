n = int(input())
count_3 = 0
last_digit = n%10
count_last_digit = 0
even_count = 0
sum_more_5 = 0
mult_7 = 1
count_0_5 = 0
while n > 0:
    x = n%10
    if x == 3:
        count_3 += 1
    if x == last_digit:
        count_last_digit += 1
    if x% 2 == 0:
        even_count += 1
    if x> 5:
        sum_more_5 = sum_more_5 + x
    if x > 7 :
        mult_7 = mult_7 * x
    if x == 0 or x == 5:
        count_0_5 += 1
    n //=10
print(count_3)
print(count_last_digit)
print(even_count)
print(sum_more_5)
print(mult_7)
print(count_0_5)
