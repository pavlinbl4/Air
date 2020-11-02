path = "//Volumes/big4photo/Downloads"
import os


def obxod(path):
    for i in os.listdir(path):
        if os.path.isdir  (path + "/" + i):
            print(path + "/" + i )
            obxod(path + "/" + i)

obxod(path)