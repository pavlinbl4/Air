from string import ascii_lowercase
# ff = "alphabet"
alphabet = { ascii_lowercase[x] : x + 1 for x in range(len(ascii_lowercase))}
for a in alphabet:
    print(a,alphabet[a])
