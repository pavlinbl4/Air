str = input()
substr = input()

index = str.find(substr)
if index == -1:
    print(index)
else:
    while index!=-1:
        print(index, end = " ")
        index = str.find(substr, (index+1))