st = input()
n = st.index(" ")
if st[0] == st[0].upper() and st[n+1] == st[n+1].upper():
    print("YES")
else:
    print("NO")
    st.sw