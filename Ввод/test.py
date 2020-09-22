while True:
    # n = input()
    n = """
    а роза 
упала на
лапу азора
 .
 """
    n = n.splitlines()
    if n == ".":
        break
    else:
        print(n.split())