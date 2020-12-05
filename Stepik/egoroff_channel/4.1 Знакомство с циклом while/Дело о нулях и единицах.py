n = int(input())
st = input()
zero = st.count("0")
one = st.count("1")
para = zero
if one < zero:
    para = one
print(n - para*2)

