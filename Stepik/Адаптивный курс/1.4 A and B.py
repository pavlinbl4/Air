tt = """A and B sat in the tree.\n
A had fallen, B was stolen.\n
What's remaining in the tree?"""
a = input()
b = input()
tt = tt.replace("A",a)
tt = tt.replace("B",b)
print(tt)
