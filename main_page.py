import time

from login_page import login_page
from signup_and_create_account import signup_and_create_account
from read_file import read_file
from utilts import clear_screen
from accounts import check_file

check_file()

accounts_list = read_file('Accounts.txt')


def main_page():
    print('-------->WELCOME<--------\n')
    choice = int(input('1) Login\n2) Create A New Account\n3) Exit\n\nchoice>> '))
    if choice == 1:
        clear_screen()
        try:
            login_page(accounts_list)
        except KeyboardInterrupt:
            clear_screen()
    elif choice == 2:
        signup_and_create_account(accounts_list)
    elif choice == 3:
        print('Exiting...')
        time.sleep(2)
        exit(0)
    else:
        clear_screen()
        print("Wrong choice. Please try again later\n")

    main_page()


if __name__ == '__main__':
    main_page()
