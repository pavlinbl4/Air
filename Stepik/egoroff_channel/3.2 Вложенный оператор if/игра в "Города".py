city1 = input().lower()
city2 = input().lower()
if city1[-1] == "ь":
    if city1[-2] == city2[0]:
        print("Good")
    else:
        print("Bad")

elif city1[-1] != "ь":

    if city1[-1] == city2[0]:
        print("Good")
    else:
        print("Bad")