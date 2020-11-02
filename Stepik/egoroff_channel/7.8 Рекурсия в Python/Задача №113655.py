"""Дана строка, содержащая только английские буквы (большие и маленькие).
Добавить символ ‘*’ (звездочка) между буквами (перед первой буквой и после последней символ ‘*’ добавлять не нужно).
входные данные
LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO
выходные данные
L*I*t*B*e*o*F*L*c*S*G*B*O*F*Q*x*M*H*o*I*u*D*D*W*c*q*c*V*g*k*c*R*o*A*e*o*c*X*O
"""

st = "LItB"
def star(st):
    if len(st) == 1:
        return st
    return st[0] + "*" + star(st[1:])
print(star(st))