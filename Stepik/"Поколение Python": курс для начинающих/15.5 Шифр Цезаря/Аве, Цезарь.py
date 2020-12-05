txt = 'Day, mice. "Year" is a mistake!'
print(txt.split())
txt = txt.split()
for i in range(len(txt)):
    shift = 0
    for x in txt[i]:
        print("txt[i] = ", txt[i])
        if x.isalpha() == True:
            shift += 1
    new = str()
    for x in txt[i]:
        if x.isalpha() == True:
            if 97 <= ord(x) <= 122 - shift:
                new = new + chr(ord(x) + shift)
            else:
                new = new + chr(shift - 25 + ord(x))
            if 65 <= ord(x) <= 90 - shift:
                new = new + chr(ord(x) + shift)
            else:
                new = new + chr(shift - 25 + ord(x))
        else:
            new = new + x
    print(new)



