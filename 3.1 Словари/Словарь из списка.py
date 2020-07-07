# """ создаем словарь из строки, где два слова разделены пробелом """
#
# s = input().split() # если слова разделены пробелом
# dc = {s[0],s[1]}
# print(dc)

""" создать слловарь в который поступают строки разделенные пробелом, до точки"""
#
# vk = {}
# while True:
#     s = input()
#     if s == ".":
#         print(vk)
#         break
#     else:
#         s = s.split(" ")
#         vk.update([s])


"""реализуем в виде функции"""

def make_vk():
    vk = {}
    while True:
        s = input()
        if s == ".":
            return vk
            #break
        else:
            s = s.split(" ")
            vk.update([s])

print(make_vk())