def test(func,arg):
    return func(func(arg))

def bolt(x):
    return x*x

print(test(bolt,2))
print(bolt,2)