import os
import sys
import time
import random
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
current_exe_dir = os.path.dirname(sys.executable)

texts = list()

def LoadTexts(filename):

    #determining whether we are running from .py or .exe
    try:
        file = open(current_file_dir+"\\"+filename,'r')
    except:
        file = open(current_exe_dir+"\\"+filename,'r')

    lines = file.readlines()
    lines = [l.strip() for l in lines]

    loadedTexts = zip(lines[::2], lines[1::2])

    for i in loadedTexts:
        #print(i)
        texts.append(i)

    file.close()

def GetRandomText():
    r = texts[random.randint(0,len(texts)-1)]
    #print(r)
    return r

LoadTexts("texts.txt")
#print(GetRandomText())
