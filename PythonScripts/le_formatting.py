from time import sleep
from os import system, name

from le_colors import colored
from le_console import clear


def is_integer(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return float(num).is_integer()


def line(line):
    sleep(0.75)
    print('\n ' + line, end = '')
    
def sub_line(line):
    sleep(0.5)
    print(' ' + line, end = '')
    
def phrase(speaker, line, color, on_color = 'on_black'):
    sleep(0.75)
    print('\n ' + colored(speaker, color, on_color) + ': ' + line, end = '')

def emote(emoter, emotion, color = 'bright_black', on_color = 'on_black'):
    sleep(0.75)
    print(colored('\n [' + emoter + ' is ' + line + ']', color, on_color), end = '')

def answer_handler(ch):
    sleep(0.5)
    print('\n')
    for i in range(1, len(ch) + 1):
        print('        ' + str(i) + ') ' + ch[i-1])
    q = False
    while not q:
        ans = input('        Ответ: ')
        if is_integer(ans) and int(ans) > 0 and int(ans) < len(ch) + 1:
            q = True
        else:
            print(colored('        Invalid input!', 'red'))
    return [int(ans), ch[int(ans)-1]]


line("Line test!")
line("Sub_Line test...")
sub_line("Completed!")
phrase("Line", "I am a simple line!", 'yellow')
emote("Line", "blushing")
