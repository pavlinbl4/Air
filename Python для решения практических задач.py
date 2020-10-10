from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
# print(s)
# ans = []
# state = 0
# for c in s[s.index("<code>"):s.index("</code>")]:
#     if c == "<code>":
#         state = 1
#     if c == "</code>":
#         state = 0
#     elif state == 0:
#         ans.append(c)
# # print(ans)
# s = "".join(ans)
# print(s)
print(s.count("</code>"))
print(s.count("<code>"))
y = 0
for x in range(4):
    print(s[s.index("<code>")+6 +y:s.index("</code>")+y])
    y += s.index("</code>") + 7
# print(s.index("<code>"))
# print(s.index('</code>'))
# print(s[s.index("<code>")+6:s.index("</code>")])
