from utilts import clear_screen


def check_file():
    try:
        # read the 'Accounts.txt' file
        # if you try to open non existing file in read mode, this will throw an error
        f = open('Accounts.txt', 'rb')
        f.close()
    except FileNotFoundError:
        # if 'Accounts.txt' file is not found, create it
        f = open('Accounts.txt', 'wb')
        f.close()


# import modules

import main_page
clear_screen()
main_page.main_page()
