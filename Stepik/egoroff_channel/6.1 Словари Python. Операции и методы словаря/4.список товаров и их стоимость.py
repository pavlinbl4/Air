price = {}
while True:
    st = input()
    if st == "конец":
        break
    else:
        data = st.split(":")
        price[int(data[1])] = data[0]
# price = {'Sony PlayStation 5': ' 46000', 'Телевизор QLED Samsung QE65Q60TAU': ' 87090', 'Смартфон Samsung Galaxy A11': ' 10000', 'Планшет Samsung Galaxy Tab S6': ' 26600'}
# with('items.txt','w') as file:
#     file.write(price)
for i in range(len(sorted(price))-1,-1,-1):
    print(price[sorted(price)[i]])

