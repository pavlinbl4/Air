"""A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts,
or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>,
а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую."""

rang = {"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
_ca = input().split()
_m = input()
if _ca[0][-1] == _ca[1][-1] and rang[_ca[0][:-1]] > rang[_ca[1][:-1]]:
    print("First")
elif _ca[0][-1] == _ca[1][-1] and rang[_ca[0][:-1]] < rang[_ca[1][:-1]]:
    print("Second")
elif _ca[0][-1] != _ca[1][-1] and _ca[0][-1] == _m:
    print("First")
elif _ca[1][-1] == _m:
    print("Second")
else:
    print("Error")

