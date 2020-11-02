n = int(input())
for i in range(1,n+1):
    st = input().lower()
    if st.find("рок") != -1:
        print(i, int(st.find("рок"))+1)