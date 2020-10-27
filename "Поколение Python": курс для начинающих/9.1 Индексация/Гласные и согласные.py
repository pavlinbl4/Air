st = input()
count_gl = 0
count_sog = 0
st = st.lower()
gl = "ауоыиэяюёе"
sog = "бвгджзйклмнпрстфхцчшщ"
for i in st:
    if i in gl:
        count_gl += 1
    elif i in sog:
        count_sog += 1
print("Количество гласных букв равно",count_gl)
print("Количество согласных букв равно",count_sog)