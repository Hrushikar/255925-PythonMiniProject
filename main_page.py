from login_page import login_page
from signup_and_create_account import signup_and_create_account
from read_file import read_file
from utilts import clear_screen
from accounts import check_file

check_file()

accounts_list = read_file('Accounts.txt')


def main_page():
    print('>>>>>>>>WELCOME<<<<<<<<\n')
    choice = int(input('1) Login\n2) Create Account\n3) Exit\n\nchoice>> '))
    if choice == 1:
        clear_screen()
        try:
            # to enable the option of (ctrl+c) to go back
            login_page(accounts_list)
        except KeyboardInterrupt:
            clear_screen()
    elif choice == 2:
        signup_and_create_account(accounts_list)
    elif choice == 3:
        # close the program
        exit(0)
    else:
        clear_screen()
        print("ERROR: Wrong choice\n")

    main_page()


if __name__ == '__main__':
    main_page()
