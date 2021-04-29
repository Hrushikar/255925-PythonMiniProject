from dashboard import dashboard
from utilts import clear_screen


def login_page(acc_list):

    login_id = input('Please, Enter your info(press "Ctrl+C" to go back) \n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            dashboard(account)
            break
        else:
            continue

    if not found:
        clear_screen()
        print('Wrong ID or Password\nWould you like to try again? (y/n)', end='')
        char = input()
        if char == 'y' or char == 'Y':
            login_page(acc_list)
        else:
            print('Exiting...')
            exit(0)

    else:
        acc_file = open('Accounts.txt', 'wb')
        print('Saving changes...')
        # after logging out of the account
        # write changes to accounts.txt file
        for acc in acc_list:
            for elements in acc:
                acc_file.write(("%s\t" % elements).encode('utf-8'))
            acc_file.write('\n'.encode('utf-8'))
