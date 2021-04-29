from utilts import clear_screen


def check_file():
    try:
        f = open('Accounts.txt', 'rb')
        f.close()
    except FileNotFoundError:
        f = open('Accounts.txt', 'wb')
        f.close()


import main_page
clear_screen()
main_page.main_page()
