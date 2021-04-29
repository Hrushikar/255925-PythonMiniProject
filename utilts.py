import os
import sys


def clear_screen():
    # function to clear the output of the screen
    # if os.name == 'nt':
    #     _ = os.system('cls')
    # else:
    #     _ = os.system('clear')
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    print('')
