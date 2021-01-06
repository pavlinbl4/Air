days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
print( *[day for day in sorted( list(filter(lambda x: len(x) == 4 or x[0] == "S",days)))],sep="\n")
# for day in sorted( list(filter(lambda x: len(x) == 4 or x[0] == "S",days))):
#     print(day)



