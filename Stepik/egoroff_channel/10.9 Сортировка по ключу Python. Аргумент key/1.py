subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
for i in sorted(subject_marks,key= lambda x:x[1]):
    print(i[0],i[1])