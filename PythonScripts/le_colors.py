def print_format_table():
    '''
    prints table of formatted text format options
    '''
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

def colored(text, foreground_color = 'white', background_color = 'on_black'):
    '''
        fg:
            black
            red
            green
            yellow
            blue
            purple
            cian
            white
            bright_black
            bright_red
            bright_green
            bright_yellow
            bright_blue
            bright_purple
            bright_cian
            bright_white
        bg:
            on_black
            on_red
            on_green
            on_yellow
            on_blue
            on_purple
            on_cian
            on_white
    '''
    FOREGROUND_COLORS = {
        'black'     : '0;30',
        'red'       : '0;31',
        'green'     : '0;32',
        'yellow'    : '0;33',
        'blue'      : '0;34',
        'purple'    : '0;35',
        'cian'      : '0;36',
        'white'     : '0;37',
        'bright_black'     : '1;30',
        'bright_red'       : '1;31',
        'bright_green'     : '1;32',
        'bright_yellow'    : '1;33',
        'bright_blue'      : '1;34',
        'bright_purple'    : '1;35',
        'bright_cian'      : '1;36',
        'bright_white'     : '1;37'
    }

    BACKGROUND_COLORS = {
        'on_black'     : '40',
        'on_red'       : '41',
        'on_green'     : '42',
        'on_yellow'    : '43',
        'on_blue'      : '44',
        'on_purple'    : '45',
        'on_cian'      : '46',
        'on_white'     : '47'
    }

    return ('\x1b[%s;%sm%s\x1b[0m' % (FOREGROUND_COLORS[foreground_color], BACKGROUND_COLORS[background_color], text))

'''
print_format_table()
print('\x1b[0;36;41m test \x1b[0m')
'''
