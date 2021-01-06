def multiply(value):
    def inner(a):
        # return value * a
        print(f"Умножение {value} на {a} =",value * a )

    return inner

