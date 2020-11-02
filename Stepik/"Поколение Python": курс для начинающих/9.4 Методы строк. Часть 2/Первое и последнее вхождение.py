txt = input()
if txt.count("f") == 0:
    print("NO")
elif txt.count("f") == 1:
    print(txt.index("f"))
else:
    print(txt.index("f"),txt.rindex("f"),sep=" ")