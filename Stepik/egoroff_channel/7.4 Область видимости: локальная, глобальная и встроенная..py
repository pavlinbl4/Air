MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age >= MIN_DRIVING_AGE:
        print(name + " может водить")
    else:
        print(name +  " еще рано садиться за руль")

allowed_driving("tin", 25)