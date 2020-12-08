# text = 'Gabler Ruby - burrel bag!'
text = text.lower()
text = text.replace("-","")
text = text.replace(" ","")
text = text.replace("?","")
text = text.replace("!","")
text = text.replace(".","")
text = text.replace(",","")
# print(text)
# text ="gablerrubyburrelbag"
flag = True
for i in range(len(text)//2):
    if text[i] == text[-i-1]:
        print(text[i],"-",text[-i-1])
        flag = True
    else:
        flag = False
        break
return flag
