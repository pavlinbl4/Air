n = int(input())
rez = []
for i in range(n):
    st = input()
    if st.find("соль") == -1:
        rez.append(st)
print(",".join(rez))