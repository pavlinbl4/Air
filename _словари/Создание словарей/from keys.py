" добавляем слова из строки по порядковому номеру"
st = " владелец  ресторана The Right  Place Роман Степанов"
voc ={}
dd = st.split()
voc = voc.fromkeys(dd,1)
print(dd)
print(voc)