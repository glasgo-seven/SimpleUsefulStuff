# version 0.4

from os import system, name
from time import sleep 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def exit():
    c = ''
    while c!='q':
        (c)

def loading(time: int):
    signs = ['|', '/', '─', '\\']
    t = 0
    while t < time:
        for sign in signs:
            clear()
            print("LOADING ", sign)
            sleep(0.2)
            t += 1
    print("LOADING COMPLETE")
    sleep(0.5)

def loadingBar(time: int):
    sing = '█'
    bar = [' ' for x in range(10)]
    
