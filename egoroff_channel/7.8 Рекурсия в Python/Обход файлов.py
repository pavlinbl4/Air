path = "//Volumes/big4photo/Downloads"
import os

def obxod(path,level = 1):
    print("level = ",level, "Content = ",os.listdir(path))
# print(os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + "/" + i):
            print(path + "/" + i )
            obxod(path + "/" + i,level +1)

obxod(path)
