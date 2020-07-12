s ="   фуфловая фура обогнала фургон"
print(type(s))
print(s.capitalize())
print("состоит строка из букв ? - ", s.isalpha())
# s1=s.replace(" ","")
# print("состоит строка из букв, не учитываем пробелы ? - ", s1.isalpha())
print(s.replace(" ","").isalpha())
print(s.strip())