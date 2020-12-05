txt = "dxy"
new = str()
shift = 4
for x in txt:
    if 97 <= ord(x) <= 122 - shift:
        new = new + chr(ord(x) + shift)
    else:
        new = new + chr(shift - 25 + ord(x))
print(new)